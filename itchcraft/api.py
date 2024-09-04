"""The primary module in itchcraft."""

from . import prefs
from .devices import find_bite_healers
from .errors import (
    BackendInitializationError,
    BiteHealerError,
    CliError,
)
from .format import format_table
from .logging import get_logger
from .prefs import (
    CliEnum,
    Duration,
    Generation,
    Preferences,
    SkinSensitivity,
)
from .start import start_with_preferences

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class Api:
    """Tech demo for interfacing with heat-based USB insect bite healers"""

    # pylint: disable=no-self-use
    def info(self) -> None:
        """Shows a list of USB bite healers that are connected to
        the host.
        """
        if not (bite_healers := list(find_bite_healers())):
            logger.info('No known bite healers detected')
            return
        logger.info(
            f'Detected {(n := len(bite_healers))}'
            + f" bite healer{'' if n == 1 else 's'}"
        )
        print(format_table(bite_healers))

    # pylint: disable=no-self-use
    def start(
        self,
        duration: CliEnum[Duration] = prefs.default(Duration),
        generation: CliEnum[Generation] = prefs.default(Generation),
        skin_sensitivity: CliEnum[SkinSensitivity] = prefs.default(
            SkinSensitivity
        ),
    ) -> None:
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
        try:
            start_with_preferences(preferences)
        except BackendInitializationError as e:
            raise CliError(e) from e
        except BiteHealerError as e:
            raise CliError(e) from e
