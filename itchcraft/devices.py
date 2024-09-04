"""Device management and discovery"""

from collections.abc import Iterator, Generator
from typing import Any, cast

import usb.core

from .device import from_usb_device, BiteHealerMetadata
from .logging import get_logger
from .support import SUPPORT_STATEMENTS, SupportStatement, VidPid

logger = get_logger(__name__)


def find_bite_healers() -> Iterator[BiteHealerMetadata]:
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
            logger.debug('Ignoring USB device %s', vid_pid)
            continue

        logger.debug('Detected bite healer %s', vid_pid)
        yield from_usb_device(
            usb_device=device,
            support_statement=statement,
        )
