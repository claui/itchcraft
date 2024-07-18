"""Backend for heat-it"""

import array
from typing import Optional, Union

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)
import usb.core  # type: ignore
import usb.util  # type: ignore

from .logging import get_logger


RESPONSE_LENGTH = 12

logger = get_logger(__name__)


class HeatItDevice:
    """A heat-it bite healer, already configured over USB."""

    dev: usb.core.Device
    endpoint_out: usb.core.Endpoint
    endpoint_in: usb.core.Endpoint

    def __init__(
        self,
        dev: usb.core.Device,
        endpoint_out: usb.core.Endpoint,
        endpoint_in: usb.core.Endpoint,
    ) -> None:
        self.dev = dev
        self.endpoint_out = endpoint_out
        self.endpoint_in = endpoint_in

    def test_bootloader(self) -> bytes:
        """Issues a `TEST_BOOTLOADER` command and returns the response."""
        return self._command([0xFF, 0xB0], 'TEST_BOOTLOADER')

    def get_status(self) -> bytes:
        """Issues a `GET_STATUS` command and returns the response."""
        return self._command([0xFF, 0x02, 0x02], 'GET_STATUS')

    def preheat(self) -> bytes:
        """Issues a `PREHEATING_TIME` command and returns the response."""
        return self._command(
            [0xFF, 0x08, 0x00, 0x00, 0x08], 'PREHEATING_TIME'
        )

    def _command(
        self,
        request: Union[list[int], bytes, bytearray],
        command_name: Optional[str] = None,
    ) -> bytes:
        if command_name is not None:
            logger.info('Sending command: %s', command_name)
        response = array.array('B', bytearray(RESPONSE_LENGTH))
        assert self.dev.write(self.endpoint_out, request) == len(
            request
        )
        assert (
            self.dev.read(self.endpoint_in, response) == RESPONSE_LENGTH
        )
        return response.tobytes()

    @retry(
        reraise=True,
        retry=retry_if_exception_type(usb.core.USBError),
        stop=stop_after_attempt(10),
        wait=wait_fixed(1),
    )
    def self_test(self) -> None:
        """Tries up to five times to test the bootloader and obtain the device status."""
        logger.debug('Response: %s', self.test_bootloader().hex(' '))
        logger.debug('Response: %s', self.get_status().hex(' '))
