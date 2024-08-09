"""Base class for devices"""

from collections.abc import Callable
from contextlib import AbstractContextManager
from dataclasses import dataclass
import functools
from typing import cast, Literal, Optional, Union

import usb.core

from .logging import get_logger
from .support import SupportStatement
from .types import BiteHealer

logger = get_logger(__name__)


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

    def connect(self) -> AbstractContextManager[BiteHealer]:
        """Connects to the device."""
        return self.connection_supplier()

    @property
    def vendor_name(self) -> str:
        """Canonical vendor name from Itchcraft’s point of view."""
        return self.support_statement.vendor_name

    @property
    def product_name(self) -> str:
        """Canonical product name from Itchcraft’s point of view."""
        return self.support_statement.product_name

    @property
    def supported(self) -> bool:
        """Whether Itchcraft supports this device."""
        return self.support_statement.supported


@dataclass(frozen=True)
class UnsupportedBiteHealerMetadata:
    """Device metadata for an unsupported bite healer connected to the
    host.
    Clients can query information from the bite healer.
    """

    usb_product_name: Optional[str]
    """Product name of the backing USB device."""

    serial_number: Optional[str]
    """Serial number of the backing USB device."""

    support_statement: SupportStatement
    """Details about the support status for this bite healer."""

    @property
    def vendor_name(self) -> str:
        """Canonical vendor name from Itchcraft’s point of view."""
        return self.support_statement.vendor_name

    @property
    def product_name(self) -> str:
        """Canonical product name from Itchcraft’s point of view."""
        return self.support_statement.product_name

    @property
    def supported(self) -> bool:
        """Whether Itchcraft supports this device."""
        return self.support_statement.supported


BiteHealerMetadata = Union[
    SupportedBiteHealerMetadata, UnsupportedBiteHealerMetadata
]


def from_usb_device(
    usb_device: usb.core.Device,
    support_statement: SupportStatement,
) -> BiteHealerMetadata:
    """Creates a metadata object from a USB device."""

    def try_get_usb_attribute(
        name: Literal['product', 'serial_number'],
    ) -> Optional[str]:
        try:
            return cast(Optional[str], getattr(usb_device, name))
        except ValueError:
            if support_statement.supported:
                logger.error(
                    '%s: cannot read `%s` attribute; check permissions',
                    support_statement.product_name,
                    name.replace('_', ' '),
                )
            return None

    if support_statement.supported is True:
        assert support_statement.connection_supplier is not None
        return SupportedBiteHealerMetadata(
            usb_product_name=try_get_usb_attribute('product'),
            serial_number=try_get_usb_attribute('serial_number'),
            connection_supplier=functools.partial(
                support_statement.connection_supplier, usb_device
            ),
            support_statement=support_statement,
        )
    return UnsupportedBiteHealerMetadata(
        usb_product_name=try_get_usb_attribute('product'),
        serial_number=try_get_usb_attribute('serial_number'),
        support_statement=support_statement,
    )
