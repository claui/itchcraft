# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring, redefined-builtin, unused-argument

from collections.abc import Iterable, Iterator
from typing import (
    Any,
    Callable,
    Literal,
    Optional,
    overload,
    TypeVar,
)

from itchcraft.types.usb import EndpointAddress

# endpoint direction
ENDPOINT_IN: int
ENDPOINT_OUT: int

D = TypeVar('D')

def endpoint_direction(
    address: EndpointAddress,
) -> Literal[0x00, 0x80]: ...
@overload
def find_descriptor(
    desc: Iterable[D],
    find_all: Literal[True],
    custom_match: Optional[Callable[[D], bool]] = ...,
    **args: dict[Any, Any],
) -> Iterator[D]: ...
@overload
def find_descriptor(
    desc: Iterable[D],
    find_all: Literal[False] = False,
    custom_match: Optional[Callable[[D], bool]] = ...,
    **args: dict[Any, Any],
) -> Optional[D]: ...
