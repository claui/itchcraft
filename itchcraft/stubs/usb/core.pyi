# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring, no-self-use, too-few-public-methods, too-many-arguments, unused-argument

from collections.abc import Iterator
import array
from typing import (
    Any,
    Callable,
    Literal,
    Optional,
    overload,
    TYPE_CHECKING,
)

import usb.backend

from itchcraft.types.usb import (
    EndpointAddress,
    EndpointIndex,
    InterfaceIndex,
    Payload,
    ProductId,
    VendorId,
)

class Configuration:
    def __getitem__(self, index: tuple[int, int]) -> 'Interface': ...

@overload
def find(
    find_all: Literal[True],
    backend: Optional[usb.backend.IBackend] = ...,
    custom_match: Optional[Callable[[Device], bool]] = ...,
    **args: dict[Any, Any],
) -> Iterator[Device]: ...
@overload
def find(
    find_all: Literal[False] = ...,
    backend: Optional[usb.backend.IBackend] = ...,
    custom_match: Optional[Callable[[Device], bool]] = ...,
    **args: dict[Any, Any],
) -> Optional[Device]: ...

# https://github.com/python/mypy/issues/5264#issuecomment-399407428
if TYPE_CHECKING:  # pylint: disable=consider-ternary-expression
    _ArrayOfInts = array.array[int]
else:
    _ArrayOfInts = array.array

class Device:
    idVendor: VendorId
    idProduct: ProductId
    product: Optional[str]
    serial_number: Optional[str]

    def get_active_configuration(self) -> Configuration: ...
    def set_configuration(
        self, configuration: Optional[Configuration] = ...
    ) -> None: ...
    def is_kernel_driver_active(
        self, interface_index: InterfaceIndex
    ) -> bool: ...
    def detach_kernel_driver(
        self, interface: InterfaceIndex
    ) -> None: ...
    @overload
    def read(
        self,
        endpoint: 'Endpoint',
        size_or_buffer: int,
        timeout: Optional[int] = ...,
    ) -> _ArrayOfInts: ...
    @overload
    def read(
        self,
        endpoint: 'Endpoint',
        size_or_buffer: Payload,
        timeout: Optional[int] = ...,
    ) -> int: ...
    def write(
        self,
        endpoint: 'Endpoint',
        data: Payload,
        timeout: Optional[int] = ...,
    ) -> int: ...

class Endpoint:
    bEndpointAddress: EndpointAddress

class Interface:
    index: InterfaceIndex
    def __iter__(self) -> Iterator[Endpoint]: ...
    def __getitem__(self, index: EndpointIndex) -> Endpoint: ...

class USBError(IOError):
    pass
