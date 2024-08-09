"""Backend for heat-it"""

from collections.abc import Iterable
from functools import reduce
from typing import Optional

from tenacity import retry
from tenacity.retry import retry_if_exception_type
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_fixed
import usb.core

from .backend import BulkTransferDevice
from .logging import get_logger
from .prefs import Preferences
from .settings import debugMode
from .types import BiteHealer, SizedPayload


RESPONSE_LENGTH = 12

logger = get_logger(__name__)


class HeatItDevice(BiteHealer):
    """A “heat it” bite healer, configured over USB."""

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

    def msg_start_heating(self, preferences: Preferences) -> bytes:
        """Issues a `MSG_START_HEATING` command and returns the
        response.
        """

        def duration_code() -> int:
            return preferences.duration.value - 1

        def generation_code() -> int:
            return preferences.generation.value - 1

        def skin_sensitivity_code() -> int:
            return preferences.skin_sensitivity.value - 1

        def payload() -> list[int]:
            return [
                0x08,
                (generation_code() << 1) + skin_sensitivity_code(),
                duration_code(),
            ]

        def checksum(payload: Iterable[int]) -> int:
            return reduce(int.__add__, payload)

        return self._command(
            [
                0xFF,
                *payload(),
                checksum(payload()),
            ],
            'MSG_START_HEATING',
        )

    def _command(
        self, request: SizedPayload, command_name: Optional[str] = None
    ) -> bytes:
        if command_name is not None:
            logger.info('Sending command: %s', command_name)
        response = self.device.bulk_transfer(request)
        assert len(response) == RESPONSE_LENGTH
        return response

    @retry(
        reraise=True,
        retry=retry_if_exception_type(usb.core.USBError),  # type: ignore
        stop=stop_after_attempt(3 if debugMode else 10),  # type: ignore
        wait=wait_fixed(1),  # type: ignore
    )
    def self_test(self) -> None:
        """Tests the bootloader and obtains the device status."""
        logger.debug('Response: %s', self.test_bootloader().hex(' '))
        logger.debug('Response: %s', self.get_status().hex(' '))

    def start_with_preferences(self, preferences: Preferences) -> None:
        """Tells the device to start heating up."""
        logger.debug(
            'Response: %s', self.msg_start_heating(preferences).hex(' ')
        )

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
