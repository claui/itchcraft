"""User preferences"""

from dataclasses import dataclass, field
from enum import Enum
import re
from typing import TypeVar, Union

from .errors import CliError

E = TypeVar('E', bound=Enum)

# If a CLI switch is backed by an enum, then allow the enum to stand in
# for that switch
CliEnum = Union[str, E]


class SkinSensitivity(Enum):
    """Whether or not a person’s skin is particularly sensitive."""

    SENSITIVE = 1
    REGULAR = 2

    def __str__(self) -> str:
        return f'{self.name.lower()} skin'


class Generation(Enum):
    """The age cohort of a person."""

    CHILD = 1
    ADULT = 2

    def __str__(self) -> str:
        return self.name.lower()


class Duration(Enum):
    """The duration of a demo session."""

    SHORT = 1
    MEDIUM = 2
    LONG = 3

    def __str__(self) -> str:
        return f'{self.name.lower()} duration'


@dataclass(frozen=True)
class Preferences:
    """User preferences for a bite healer demo session."""

    skin_sensitivity: SkinSensitivity = field(
        default=SkinSensitivity.SENSITIVE
    )
    generation: Generation = field(default=Generation.CHILD)
    duration: Duration = field(default=Duration.SHORT)

    def __str__(self) -> str:
        return ', '.join(
            str(attr)
            for attr in (
                self.duration,
                self.generation,
                self.skin_sensitivity,
            )
        )


def default(enum_type: type[E]) -> str:
    """Returns the default preference for a given Enum type.

    :param enum_type:
        Enum type which exists as an attribute in Preferences and
        whose corresponding attribute name is equal to the type name
        converted to snake case.
    """
    default_value: E = getattr(Preferences, _snake_case_name(enum_type))
    return default_value.name.lower()


# pylint: disable=raise-missing-from
def parse(value: CliEnum[E], enum_type: type[E]) -> E:
    """Parses a given value into an Enum if it isn’t one yet.
    Returns the value itself if it’s already an Enum.

    :param value:
        an Enum value or a corresponding name, written in lower case.

    :param enum_type:
        the type of the Enum to parse into.
    """
    if isinstance(value, enum_type):
        return value
    assert isinstance(value, str)
    try:
        return enum_type[value.upper()]
    except KeyError:
        raise CliError(
            f'Invalid value `{value}`. Valid values for {_snake_case_name(enum_type)} are: '
            + ', '.join([key.lower() for key in enum_type.__members__]),
        )


def _snake_case_name(camel_case_type: type) -> str:
    """Returns the name of the given type converted into snake case."""
    return re.sub(
        r'(?:\B|\Z)([A-Z])',
        lambda match: f'_{match.group(1)}',
        camel_case_type.__name__,
    ).lower()
