"""User preferences"""

from dataclasses import dataclass, field
from enum import Enum
import re
from typing import TypeVar, Union

from .errors import CliError

_E = TypeVar('_E', bound=Enum)

CliEnum = Union[str, _E]
"""Helper union type consisting of an :py:class:`~enum.Enum` and its stringified values.

If a command line switch is backed by an `Enum`, then allow the enum
to stand in for that switch.

For example, if you have the following `Enum` class:

.. code:: python

    from enum import Enum

    class Widget(Enum):
        FOO = 1
        BAR = 2

and an associated command line switch ``--widget``, which can take the
form of either ``--widget foo`` and ``--widget bar``, then
`CliEnum[Widget]` means that the four values ``Widget.FOO``,
``Widget.BAR``, ``"foo"``, and ``"bar"`` should be accepted.

`Widget.FOO` is equivalent to ``"foo"``, while `Widget.BAR` stands in
for ``"bar"``:

.. code:: python

    from itchcraft.prefs import CliEnum, parse

    def frob(widget: CliEnum[Widget]) -> None:
        real_widget: Widget = parse(widget, Widget)
        ...

    frob("foo")
    frob("bar")
    frob(Widget.FOO)  # same as frob("foo")
    frob(Widget.BAR)  # same as frob("bar")

"""


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


def default(enum_type: type[_E]) -> str:
    """Returns the default preference for a given :py:class:`~enum.Enum` type.

    :param enum_type:
        Enum type which exists as an attribute in
        :py:class:`.Preferences` and whose corresponding attribute name
        is equal to the type name converted to snake case.
    """
    default_value: _E = getattr(
        Preferences, _snake_case_name(enum_type)
    )
    return default_value.name.lower()


# pylint: disable=raise-missing-from
def parse(value: CliEnum[_E], enum_type: type[_E]) -> _E:
    """Parses a given value into an :py:class:`~enum.Enum` if it isn’t one yet.

    :param value:
        an `Enum` value or a corresponding name, written in lower case.

    :param enum_type:
        the type of the `Enum` to parse into.

    :return:
        an instance of `enum_type` that represents `value`.
        If `value` is already an instance of `enum_type`, then the
        return value is `value` itself.
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
