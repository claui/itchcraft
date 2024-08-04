"""Device management and discovery"""

from collections.abc import Iterator, Generator
from typing import Any, cast

import usb.core  # type: ignore

from .device import SupportedBiteHealerMetadata
from .support import SUPPORT_STATEMENTS, SupportStatement, VidPid


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
                support_statement=statement,
            )
