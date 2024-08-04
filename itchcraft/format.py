"""Formatting support"""

from collections.abc import Iterable

from .device import SupportedBiteHealerMetadata


def format_table(
    bite_healers: Iterable[SupportedBiteHealerMetadata],
) -> str:
    """Returns a formatted table for the given list of bite healers."""
    return '\n'.join(
        [
            f'{format_title(item)}'
            + f" – {'supported' if item.supported() else 'unsupported'}"
            for item in bite_healers
        ]
    )


def format_title(item: SupportedBiteHealerMetadata) -> str:
    """Returns a formatted title for the given bite healer."""

    def details() -> list[str]:
        return (
            [
                f'S/N: {item.serial_number}',
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
            '*',
            item.product_name,
            f"({', '.join(details())})",
        ]
    )
