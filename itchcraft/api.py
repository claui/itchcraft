"""The primary module in itchcraft."""

from contextlib import ExitStack

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

        with ExitStack() as stack:
            candidates = [
                stack.enter_context(candidate)
                for candidate in find_devices()
            ]
            if not candidates:
                raise CliError('No bite healer connected')

            device = candidates[0]
            logger.info('Using device: %s', device)
            for rejected_device in candidates[1:]:
                logger.info(
                    'Ignoring additional device: %s', rejected_device
                )
                logger.warning(
                    'Itchcraft can only use one device at a time.'
                )

            device.self_test()
            device.start_heating()
