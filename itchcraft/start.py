"""Activates a connected USB bite healer."""

from contextlib import ExitStack

from . import devices
from .errors import BiteHealerError
from .logging import get_logger
from .prefs import Preferences

logger = get_logger(__name__)


def start_with_prefs(preferences: Preferences) -> None:
    """Activates (i.e. heats up) a connected USB bite healer for
    demonstration purposes.

    :param preferences:
        User preferences for the settings of the bite healer.
    """
    logger.warning('This app is only a tech demo')
    logger.warning('and NOT for medical use.')
    logger.warning('The app is NOT SAFE to use')
    logger.warning('for treating insect bites.')

    logger.info('Searching for bite healer')

    with ExitStack() as stack:
        candidates = [
            stack.enter_context(candidate)
            for candidate in devices.find_devices()
        ]
        if not candidates:
            raise BiteHealerError('No bite healer connected')

        device = candidates[0]
        logger.info('Using device: %s', device)
        for rejected_device in candidates[1:]:
            logger.info(
                'Ignoring additional device: %s', rejected_device
            )
            logger.warning(
                'Itchcraft can only use one device at a time.'
            )

        logger.info('Using settings: %s', preferences)
        device.self_test()
        device.start_heating(preferences)
