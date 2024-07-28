"""The primary module in itchcraft."""

from typing import Optional

from .device import Device
from .devices import find_devices
from .errors import CliError
from .logging import get_logger

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class Api:
    """Tech demo for interfacing with heat-based USB insect bite healers"""

    def start(self) -> None:  # pylint: disable=no-self-use
        """Activates (i.e. heats up) a connected USB bite healer for
        demonstration purposes.
        """

        logger.warning('This app is only a tech demo')
        logger.warning('and NOT for medical use.')
        logger.warning('The app is NOT SAFE to use')
        logger.warning('for treating insect bites.')

        logger.info('Searching for bite healer')

        device: Optional[Device] = None

        for init_candidate in find_devices():
            with init_candidate as candidate:
                if device is not None:
                    logger.info('Ignoring device: %s', candidate)
                    continue
                device = candidate
                logger.info('Using device: %s', device)
                device.self_test()
                device.start_heating()

        if device is None:
            raise CliError('No bite healer connected')
