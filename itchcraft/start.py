"""Activates a connected USB bite healer."""

from typing import cast

from . import devices
from .device import SupportedBiteHealerMetadata
from .errors import BiteHealerError
from .format import format_title
from .logging import get_logger
from .prefs import Preferences

logger = get_logger(__name__)


def start_with_preferences(preferences: Preferences) -> None:
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

    if not (candidates := list(devices.find_bite_healers())):
        raise BiteHealerError('No bite healer connected')
    supported_candidates: list[SupportedBiteHealerMetadata] = [
        cast(SupportedBiteHealerMetadata, candidate)
        for candidate in candidates
        if candidate.supported
    ]
    if not supported_candidates:
        raise BiteHealerError(
            f'Unsupported bite healer: {format_title(candidates[0])}.'
            + ' Please raise an issue on Itchcraft’s project page.'
        )
    candidate = supported_candidates[0]
    assert candidate.supported is True

    logger.info('Using bite healer: %s', format_title(candidate))
    logger.info('Using settings: %s', preferences)

    with candidate.connect() as bite_healer:
        bite_healer.self_test()
        bite_healer.start_with_preferences(preferences)
