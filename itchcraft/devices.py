"""Device management and discovery"""

from collections.abc import Iterator, Generator
from contextlib import AbstractContextManager, contextmanager
from dataclasses import dataclass
from typing import Any, Callable, cast, NamedTuple, Optional

import usb.core  # type: ignore

from .backend import UsbBulkTransferDevice
from .device import BiteHealer, SupportedBiteHealerMetadata
from .heat_it import HeatItDevice


@dataclass(frozen=True)
class SupportStatement:
    """Statement that establishes whether or not a given combination
    of vendor ID (VID) and product id (PID) is a supported bite healer,
    and which model it is."""

    vid: int
    """USB vendor ID"""
    pid: int
    """USB product ID"""
    name: str
    """Canonical model name from Itchcraft’s point of view"""
    supported: bool = True
    """Whether or not Itchcraft supports this model"""
    comment: Optional[str] = None
    """Additional comments on the support status of this model"""
    connection_supplier: Optional[
        Callable[[usb.core.Device], AbstractContextManager[BiteHealer]]
    ] = None
    """Callable that establishes a connection to this model"""


class VidPid(NamedTuple):
    """Tuple of USB vendor ID (VID) and product ID (PID)."""

    vid: int
    pid: int


@contextmanager
def _heat_it_device(
    usb_device: usb.core.Device,
) -> Iterator[HeatItDevice]:
    yield HeatItDevice(UsbBulkTransferDevice(usb_device))


SUPPORT_STATEMENTS: list[SupportStatement] = [
    SupportStatement(
        vid=0x32F9,
        pid=0xFCBA,
        name='heat it',
        connection_supplier=_heat_it_device,
    ),
]


def find_bite_healers() -> Iterator[SupportedBiteHealerMetadata]:
    """Finds available bite healers."""
    devices = cast(
        Generator[usb.core.Device, Any, None],
        usb.core.find(find_all=True),
    )
    vid_pid_dict: dict[VidPid, SupportStatement] = {
        VidPid(vid=statement.vid, pid=statement.pid): statement
        for statement in SUPPORT_STATEMENTS
    }

    for device in devices:
        vid_pid = VidPid(vid=device.idVendor, pid=device.idProduct)

        if (statement := vid_pid_dict.get(vid_pid)) is None:
            continue

        if statement.supported:
            assert statement.connection_supplier is not None
            yield SupportedBiteHealerMetadata.from_usb_device(
                usb_device=device,
                connection_supplier=statement.connection_supplier,
            )
