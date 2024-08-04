"""USB backend management"""

from abc import ABC, abstractmethod
import array
from collections.abc import Callable
from typing import Optional, Union, cast

import usb.core  # type: ignore

from .errors import BackendInitializationError, EndpointNotFound


class BulkTransferDevice(ABC):
    """Abstract base class for USB devices with two bulk transfer
    endpoints."""

    @abstractmethod
    def bulk_transfer(
        self,
        request: Union[list[int], bytes, bytearray],
    ) -> bytes:
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
        device.set_configuration()
        config = cast(
            usb.core.Configuration,
            device.get_active_configuration(),
        )
        interface = config[(0, 0)]

        self.device = device
        try:
            self.endpoint_out = _find_endpoint(interface, _match_out)
        except EndpointNotFound as ex:
            raise BackendInitializationError(
                f'Outbound endpoint not found for {device}',
            ) from ex
        try:
            self.endpoint_in = _find_endpoint(interface, _match_in)
        except EndpointNotFound as ex:
            raise BackendInitializationError(
                f'Inbound endpoint not found for {device}',
            ) from ex

    def bulk_transfer(
        self,
        request: Union[list[int], bytes, bytearray],
    ) -> bytes:
        response = array.array('B', bytearray(self.MAX_RESPONSE_LENGTH))
        assert self.device.write(self.endpoint_out, request) == len(
            request
        )
        bytes_received = self.device.read(self.endpoint_in, response)
        return response[:bytes_received].tobytes()

    @property
    def product_name(self) -> Optional[str]:
        return cast(Optional[str], self.device.product)

    @property
    def serial_number(self) -> Optional[str]:
        return cast(Optional[str], self.device.serial_number)


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
    return cast(usb.core.Endpoint, endpoint)


def _match_in(endpoint: usb.core.Endpoint) -> bool:
    address = endpoint.bEndpointAddress  # pyright: ignore
    return bool(
        usb.util.endpoint_direction(address) == usb.util.ENDPOINT_IN
    )


def _match_out(device: usb.core.Device) -> bool:
    address = device.bEndpointAddress  # pyright: ignore
    return bool(
        usb.util.endpoint_direction(address) == usb.util.ENDPOINT_OUT
    )
