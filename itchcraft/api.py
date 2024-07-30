"""The primary module in itchcraft."""

from contextlib import ExitStack
from dataclasses import dataclass

from . import devices, prefs
from .errors import CliError
from .logging import get_logger
from .prefs import (
    CliEnum,
    Duration,
    Generation,
    Preferences,
    SkinSensitivity,
)

logger = get_logger(__name__)


@dataclass(frozen=True)
class StartParams:
    """Parameters for the `start` method or CLI subcommand."""

    duration: CliEnum[Duration] = prefs.default(Duration)
    generation: CliEnum[Generation] = prefs.default(Generation)
    skin_sensitivity: CliEnum[SkinSensitivity] = prefs.default(
        SkinSensitivity
    )


# pylint: disable=too-few-public-methods
class Api:
    """Tech demo for interfacing with heat-based USB insect bite healers"""

    # pylint: disable=no-self-use
    def start(
        self,
        # Re-enumerating all the `StartParams` fields to make Fire happy
        duration: CliEnum[Duration] = prefs.default(Duration),
        generation: CliEnum[Generation] = prefs.default(Generation),
        skin_sensitivity: CliEnum[SkinSensitivity] = prefs.default(
            SkinSensitivity
        ),
    ) -> None:  # pylint: disable=no-self-use
        """Activates (i.e. heats up) a connected USB bite healer for
        demonstration purposes.

        :param duration:
            One of `short`, `medium`, or `long`.

        :param generation:
            `child` or `adult`.

        :param skin_sensitivity:
            `regular` or `sensitive`.
        """

        preferences = Preferences(
            duration=prefs.parse(duration, Duration),
            generation=prefs.parse(generation, Generation),
            skin_sensitivity=prefs.parse(
                skin_sensitivity, SkinSensitivity
            ),
        )
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

            logger.info('Using settings: %s', preferences)
            device.self_test()
            device.start_heating(preferences)
