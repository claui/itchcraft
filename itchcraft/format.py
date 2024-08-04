"""Formatting support"""

from collections.abc import Iterable
from operator import attrgetter

from .device import BiteHealerMetadata


def format_table(
    bite_healers: Iterable[BiteHealerMetadata],
) -> str:
    """Returns a formatted table for the given list of bite healers."""
    return '\n'.join(
        [
            ('[*]' if item.supported else '[!]')
            + f' {format_title(item)}'
            + f" – {'supported' if item.supported else 'unsupported'}"
            for item in sorted(
                bite_healers,
                key=attrgetter('supported'),
                reverse=True,
            )
        ]
    )


def format_title(item: BiteHealerMetadata) -> str:
    """Returns a formatted title for the given bite healer."""

    def details() -> list[str]:
        return (
            [
                (
                    f'S/N: {item.serial_number}'
                    if item.serial_number
                    else 'unknown serial number'
                ),
            ]
            + (
                [f'self-identified as `{item.usb_product_name}`']
                if item.usb_product_name
                else []
            )
            + [
                f'vendor: {item.vendor_name}',
            ]
        )

    return ' '.join(
        [
            item.product_name,
            f"({', '.join(details())})",
        ]
    )
