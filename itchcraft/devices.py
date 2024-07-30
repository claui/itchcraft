"""Device management and discovery"""

from collections.abc import Iterator, Generator
from contextlib import AbstractContextManager, contextmanager
from typing import Any, cast

import usb.core  # type: ignore

from .backend import UsbBulkTransferDevice
from .heat_it import HeatItDevice
from .device import Device


def find_devices() -> Iterator[AbstractContextManager[Device]]:
    """Finds the first available backend"""
    devices = cast(
        Generator[usb.core.Device, Any, None],
        usb.core.find(find_all=True, idVendor=0x32F9, idProduct=0xFCBA),
    )
    for usb_device in devices:
        yield _heat_it_device(usb_device)


@contextmanager
def _heat_it_device(
    usb_device: usb.core.Device,
) -> Iterator[HeatItDevice]:
    yield HeatItDevice(UsbBulkTransferDevice(usb_device))
