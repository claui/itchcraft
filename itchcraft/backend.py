"""USB backend management"""

from abc import ABC, abstractmethod
import array
from collections.abc import Callable
from typing import Optional

import usb.core
import usb.util

from .errors import BackendInitializationError, EndpointNotFound
from .logging import get_logger
from .types import SizedPayload, usb as usb_types

logger = get_logger(__name__)


class BulkTransferDevice(ABC):
    """Abstract base class for USB devices with two bulk transfer
    endpoints."""

    @abstractmethod
    def bulk_transfer(self, request: SizedPayload) -> bytes:
        """Sends a payload via USB bulk transfer and waits for a response
        from the device.

        :param `request`: the request payload from the host.

        :return: the response received from the device.
        """

    @property
    @abstractmethod
    def product_name(self) -> Optional[str]:
        """Product name of the device that this backend represents."""

    @property
    @abstractmethod
    def serial_number(self) -> Optional[str]:
        """Serial number of the device that this backend represents."""


class UsbBulkTransferDevice(BulkTransferDevice):
    """USB device with two bulk transfer endpoints."""

    MAX_RESPONSE_LENGTH = 12

    device: usb.core.Device
    endpoint_out: usb.core.Endpoint
    endpoint_in: usb.core.Endpoint

    def __init__(self, device: usb.core.Device) -> None:
        if (config := _get_config_if_exists(device)) is None:
            try:
                device.set_configuration()
            except usb.core.USBError as ex:
                raise BackendInitializationError(
                    f'Unable to connect to {device.product}: {ex}'
                ) from ex
            logger.debug('Configuration successful')
            config = device.get_active_configuration()

        interface = config[(0, 0)]
        self.device = device

        _detach_driver_if_needed(device, interface.index)

        try:
            self.endpoint_out = _find_endpoint(interface, _match_out)
        except EndpointNotFound as ex:
            raise BackendInitializationError(
                f'Outbound endpoint not found for {device.product}',
            ) from ex
        logger.debug('Found outbound endpoint: %s', self.endpoint_out)
        try:
            self.endpoint_in = _find_endpoint(interface, _match_in)
        except EndpointNotFound as ex:
            raise BackendInitializationError(
                f'Inbound endpoint not found for {device.product}',
            ) from ex
        logger.debug('Found inbound endpoint: %s', self.endpoint_in)

    def bulk_transfer(self, request: SizedPayload) -> bytes:
        buffer = array.array('B', bytearray(self.MAX_RESPONSE_LENGTH))
        assert self.device.write(self.endpoint_out, request) == len(
            request
        )
        num_bytes_received = self.device.read(self.endpoint_in, buffer)
        response = buffer[:num_bytes_received].tobytes()
        logger.debug(
            'Got response: %s (%s)', response.hex(' '), response
        )
        return response

    @property
    def product_name(self) -> Optional[str]:
        return self.device.product

    @property
    def serial_number(self) -> Optional[str]:
        return self.device.serial_number


def _detach_driver_if_needed(
    device: usb.core.Device, interface_index: usb_types.InterfaceIndex
) -> None:
    try:
        want_to_detach_driver = device.is_kernel_driver_active(
            interface_index
        )
    except NotImplementedError:
        logger.debug(
            'Note: unable to detach driver for interface #%d; proceeding',
            interface_index,
        )
        want_to_detach_driver = False

    if not want_to_detach_driver:
        return

    logger.debug(
        'Detaching driver from interface #%d',
        interface_index,
    )
    device.detach_kernel_driver(interface_index)
    logger.debug('Driver successfully detached')


def _find_endpoint(
    interface: usb.core.Interface,
    custom_match: Callable[[usb.core.Endpoint], bool],
) -> usb.core.Endpoint:
    if (
        endpoint := usb.util.find_descriptor(
            interface,
            custom_match=custom_match,
        )
    ) is None:
        raise EndpointNotFound('find_descriptor returned None')
    return endpoint


def _get_config_if_exists(
    device: usb.core.Device,
) -> Optional[usb.core.Configuration]:
    try:
        config = device.get_active_configuration()
    except usb.core.USBError:
        logger.debug('Device has no active configuration')
        config = None
    else:
        logger.debug('Device already configured')
        logger.debug('Active configuration: %s', config)
    return config


def _match_in(endpoint: usb.core.Endpoint) -> bool:
    address = endpoint.bEndpointAddress
    return bool(
        usb.util.endpoint_direction(address) == usb.util.ENDPOINT_IN
    )


def _match_out(endpoint: usb.core.Endpoint) -> bool:
    address = endpoint.bEndpointAddress
    return bool(
        usb.util.endpoint_direction(address) == usb.util.ENDPOINT_OUT
    )
