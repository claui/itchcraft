"""Declaring supported bite healers"""

from collections.abc import Iterator
from contextlib import AbstractContextManager, contextmanager
from dataclasses import dataclass
from typing import Callable, NamedTuple, Optional

import usb.core

from .backend import UsbBulkTransferDevice
from .heat_it import HeatItDevice
from .types import BiteHealer


@dataclass(frozen=True)
class SupportStatement:
    """Statement that establishes whether or not a given combination
    of vendor ID (VID) and product id (PID) is a supported bite healer,
    and which model it is."""

    vid: int
    """USB vendor ID"""
    pid: int
    """USB product ID"""
    vendor_name: str
    """Canonical vendor name from Itchcraft’s point of view"""
    product_name: str
    """Canonical product name from Itchcraft’s point of view"""
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

    def __str__(self) -> str:
        return (
            f'{self.vid:04x}:{self.pid:04x}'
            + f' (VID {self.vid}, PID {self.pid})'
        )


@contextmanager
def _heat_it_device(
    usb_device: usb.core.Device,
) -> Iterator[HeatItDevice]:
    yield HeatItDevice(UsbBulkTransferDevice(usb_device))


_UNTESTED = """\
Itchcraft hasn’t been tested on this model, but I expect it to work just
fine. Your feedback is welcome, so feel free to open a GitHub issue on
https://github.com/claui/itchcraft/issues and share your findings.
Or write to: itchcraft@cpellegrino.de
"""


SUPPORT_STATEMENTS: list[SupportStatement] = [
    # Supported bite healers
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0001,  # 1
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0002,  # 2
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0003,  # 3
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0004,  # 4
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0005,  # 5
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0006,  # 6
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0xFCA9,  # 64681
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
        comment=_UNTESTED,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0xFCBA,  # 64698
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        connection_supplier=_heat_it_device,
    ),
    # Unsupported bite healers
    SupportStatement(
        vid=0x10C4,  # 4292
        pid=0x8C9B,  # 35995
        vendor_name='Kamedi GmbH',
        product_name='heat it (legacy)',
        supported=False,
        comment='Itchcraft doesn’t work with this legacy model.',
    ),
    SupportStatement(
        vid=0x10C4,  # 4292
        pid=0xEA60,  # 60000
        vendor_name='mibeTec GmbH',
        product_name='bite away® pro',
        supported=False,
        comment="""\
        Support for this model is on the roadmap for a future release
        of Itchcraft.
        """,
    ),
    SupportStatement(
        vid=0x10C4,  # 4292
        pid=0xEAC9,  # 60105
        vendor_name='Silicon Laboratories, Inc.',
        product_name='EFM8UB1',
        supported=False,
        comment="""\
        Stock EFM8 chipset; missing bite healer firmware.
        Can’t be used as a bite healer unless firmware is installed.
        """,
    ),
    SupportStatement(
        vid=0x32F9,  # 13049
        pid=0x0007,  # 7
        vendor_name='Kamedi GmbH',
        product_name='heat it',
        supported=False,
        comment="""\
        Itchcraft is not compatible with this new model. If you’d like
        me to add support, please open a GitHub issue on
        https://github.com/claui/itchcraft/issues or write to:
        itchcraft@cpellegrino.de
        """,
    ),
]
