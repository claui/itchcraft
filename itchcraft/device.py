"""Base class for devices"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from contextlib import AbstractContextManager
from dataclasses import dataclass
import functools
from typing import cast, Optional, TypeVar

import usb.core  # type: ignore

from .prefs import Preferences


class BiteHealer(ABC):
    """Abstraction for a bite healer."""

    @abstractmethod
    def self_test(self) -> None:
        """Tests the device to make sure it is online and
        functional."""

    @abstractmethod
    def start_with_preferences(self, preferences: Preferences) -> None:
        """Tells the device to start heating up."""


Self = TypeVar('Self', bound='SupportedBiteHealerMetadata')


@dataclass(frozen=True)
class SupportedBiteHealerMetadata:
    """Device metadata for a supported bite healer connected to the
    host but not necessarily activated.
    Clients can query information from the bite healer and open a
    connection.
    """

    product_name: Optional[str]
    """Product name of the backing USB device."""

    serial_number: Optional[str]
    """Serial number of the backing USB device."""

    connection_supplier: Callable[
        [], AbstractContextManager[BiteHealer]
    ]
    """Callable that connects to the bite healer."""

    @classmethod
    def from_usb_device(
        cls: type[Self],
        usb_device: usb.core.Device,
        connection_supplier: Callable[
            [usb.core.Device], AbstractContextManager[BiteHealer]
        ],
    ) -> Self:
        """Creates a metadata object from a USB device."""

        return cls(
            product_name=cast(Optional[str], usb_device.product),
            serial_number=cast(Optional[str], usb_device.serial_number),
            connection_supplier=functools.partial(
                connection_supplier, usb_device
            ),
        )

    def connect(self) -> AbstractContextManager[BiteHealer]:
        """Connects to the device."""
        return self.connection_supplier()

    @staticmethod
    def supported() -> bool:
        """Whether Itchcraft supports this device."""
        return True
