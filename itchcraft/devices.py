"""Device management and discovery"""

from collections.abc import Iterator, Generator
from contextlib import contextmanager
from typing import Any, cast

import usb.core  # type: ignore

from .backend import UsbBulkTransferDevice
from .device import SupportedBiteHealerMetadata
from .heat_it import HeatItDevice


def find_bite_healers() -> Iterator[SupportedBiteHealerMetadata]:
    """Finds available bite healers."""
    devices = cast(
        Generator[usb.core.Device, Any, None],
        usb.core.find(find_all=True, idVendor=0x32F9, idProduct=0xFCBA),
    )
    for usb_device in devices:
        yield SupportedBiteHealerMetadata.from_usb_device(
            usb_device=usb_device,
            connection_supplier=_heat_it_device,
        )


@contextmanager
def _heat_it_device(
    usb_device: usb.core.Device,
) -> Iterator[HeatItDevice]:
    yield HeatItDevice(UsbBulkTransferDevice(usb_device))
