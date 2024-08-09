# pylint: disable=missing-class-docstring

"""Auxiliary types used by both Itchcraft’s USB typing stubs and
by Itchcraft itself.
"""

from collections.abc import Iterable
from typing import NewType, Union

EndpointIndex = NewType('EndpointIndex', int)
EndpointAddress = NewType('EndpointAddress', int)
InterfaceIndex = NewType('InterfaceIndex', int)
Payload = Union[bytes, Iterable[int]]

VendorId = NewType('VendorId', int)
ProductId = NewType('ProductId', int)
