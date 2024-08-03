"""Formatting support"""

from .device import SupportedBiteHealerMetadata


def format_title(metadata: SupportedBiteHealerMetadata) -> str:
    """Returns a formatted title for the device."""
    name: str = metadata.product_name or 'unknown'
    return f'{name}  (S/N: {metadata.serial_number})'
