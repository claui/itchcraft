"""Backend for heat-it"""

from typing import Optional, Union

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)
import usb.core  # type: ignore

from .backend import BulkTransferDevice
from .device import Device
from .logging import get_logger


RESPONSE_LENGTH = 12

logger = get_logger(__name__)


class HeatItDevice(Device):
    """A heat-it bite healer, configured over USB."""

    device: BulkTransferDevice

    def __init__(self, device: BulkTransferDevice) -> None:
        self.device = device

    def test_bootloader(self) -> bytes:
        """Issues a `TEST_BOOTLOADER` command and returns the
        response.
        """
        return self._command([0xFF, 0xB0], 'TEST_BOOTLOADER')

    def get_status(self) -> bytes:
        """Issues a `GET_STATUS` command and returns the response."""
        return self._command([0xFF, 0x02, 0x02], 'GET_STATUS')

    def msg_start_heating(self) -> bytes:
        """Issues a `MSG_START_HEATING` command and returns the
        response.
        """
        return self._command(
            [0xFF, 0x08, 0x00, 0x00, 0x08], 'MSG_START_HEATING'
        )

    def _command(
        self,
        request: Union[list[int], bytes, bytearray],
        command_name: Optional[str] = None,
    ) -> bytes:
        if command_name is not None:
            logger.info('Sending command: %s', command_name)
        response = self.device.bulk_transfer(request)
        assert len(response) == RESPONSE_LENGTH
        return response

    @retry(
        reraise=True,
        retry=retry_if_exception_type(usb.core.USBError),
        stop=stop_after_attempt(10),
        wait=wait_fixed(1),
    )
    def self_test(self) -> None:
        """Tries up to five times to test the bootloader and obtain
        the device status.
        """
        logger.debug('Response: %s', self.test_bootloader().hex(' '))
        logger.debug('Response: %s', self.get_status().hex(' '))

    def start_heating(self) -> None:
        """Tells the device to start heating up."""
        logger.debug('Response: %s', self.msg_start_heating().hex(' '))

        logger.info('Device now preheating.')
        logger.info('Watch the LED closely.')
        logger.info('It will blink purple, then stop')
        logger.info('and light up blue.')

        logger.warning('While using this app, your')
        logger.warning('bite healer is NOT SAFE for')
        logger.warning('use on human skin.')

        logger.info('Once the LED turns green,')
        logger.info('the tech demo has completed.')

    def __str__(self) -> str:
        name: str = (
            self.device.product_name
            or 'unknown, self-identifies as heat-it'
        )
        return f'{name}  (S/N: {self.device.serial_number})'
