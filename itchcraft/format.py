"""Formatting support"""

from collections.abc import Iterable, Iterator
from operator import attrgetter
import shutil
from textwrap import dedent, fill, TextWrapper

from colorama import Fore, Style

from .device import BiteHealerMetadata


def format_table(
    bite_healers: Iterable[BiteHealerMetadata],
) -> str:
    """Returns a formatted table for the given list of bite healers."""

    comment_wrapper = TextWrapper(
        width=max_line_width(),
        initial_indent='    ^ ',
        subsequent_indent='      ',
    )

    def format_table_entry_header(item: BiteHealerMetadata) -> str:
        return (
            format_title(item)
            + ' '
            + (
                f'{Fore.GREEN}[supported]{Style.RESET_ALL}'
                if item.supported
                else f'{Fore.YELLOW}[unsupported]{Style.RESET_ALL}'
            )
        )

    def format_entry_comment(item: BiteHealerMetadata) -> str:
        assert item.support_statement.comment is not None
        return (
            (Fore.GREEN if item.supported else Fore.YELLOW)
            + comment_wrapper.fill(
                dedent(item.support_statement.comment)
            )
            + Style.RESET_ALL
        )

    def generate_lines() -> Iterator[str]:
        for item in sorted(
            bite_healers,
            key=attrgetter('supported'),
            reverse=True,
        ):
            yield fill(
                format_table_entry_header(item),
                width=max_line_width(),
                initial_indent=(
                    f'{Fore.GREEN}[*]{Style.RESET_ALL} '
                    if item.supported
                    else f'{Fore.YELLOW}[!]{Style.RESET_ALL} '
                ),
                subsequent_indent='    ',
            )
            if item.support_statement.comment is not None:
                yield format_entry_comment(item)

    return '\n'.join(generate_lines())


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
            f'{Style.BRIGHT}{item.product_name}{Style.RESET_ALL}',
            f"{Style.DIM}({', '.join(details())}){Style.RESET_ALL}",
        ]
    )


def max_line_width() -> int:
    """Returns the maximum width (in terminal columns) to be used
    when formatting text.
    """
    return shutil.get_terminal_size().columns or 70
