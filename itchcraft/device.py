"""Base class for devices"""

from collections.abc import Callable
from contextlib import AbstractContextManager
from dataclasses import dataclass
import functools
from typing import cast, Optional, TypeVar

import usb.core  # type: ignore

from .support import SupportStatement
from .types import BiteHealer


_Self = TypeVar('_Self', bound='SupportedBiteHealerMetadata')


@dataclass(frozen=True)
class SupportedBiteHealerMetadata:
    """Device metadata for a supported bite healer connected to the
    host but not necessarily activated.
    Clients can query information from the bite healer and open a
    connection.
    """

    usb_product_name: Optional[str]
    """Product name of the backing USB device."""

    serial_number: Optional[str]
    """Serial number of the backing USB device."""

    connection_supplier: Callable[
        [], AbstractContextManager[BiteHealer]
    ]
    """Callable that connects to the bite healer."""

    support_statement: SupportStatement
    """Details about the support status for this bite healer."""

    @classmethod
    def from_usb_device(
        cls: type[_Self],
        usb_device: usb.core.Device,
        support_statement: SupportStatement,
    ) -> _Self:
        """Creates a metadata object from a USB device."""

        assert support_statement.supported is True
        assert support_statement.connection_supplier is not None
        return cls(
            usb_product_name=cast(Optional[str], usb_device.product),
            serial_number=cast(Optional[str], usb_device.serial_number),
            connection_supplier=functools.partial(
                support_statement.connection_supplier, usb_device
            ),
            support_statement=support_statement,
        )

    def connect(self) -> AbstractContextManager[BiteHealer]:
        """Connects to the device."""
        return self.connection_supplier()

    @property
    def vendor_name(self) -> str:
        """Canonical vendor name from Itchcraft’s point of view"""
        return self.support_statement.vendor_name

    @property
    def product_name(self) -> str:
        """Canonical product name from Itchcraft’s point of view"""
        return self.support_statement.product_name

    @staticmethod
    def supported() -> bool:
        """Whether Itchcraft supports this device."""
        return True
