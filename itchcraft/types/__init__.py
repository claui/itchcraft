"""Types used in several places"""

from abc import ABC, abstractmethod
from collections.abc import Collection
from typing import Union

from ..prefs import Preferences


SizedPayload = Union[bytes, Collection[int]]
"""Helper union type consisting of :py:class:`bytes` and :py:class:`collections.abc.Collection[int]`.
"""  # pylint: disable=line-too-long


class BiteHealer(ABC):
    """Abstraction for a bite healer."""

    @abstractmethod
    def self_test(self) -> None:
        """Tests the device to make sure it is online and
        functional."""

    @abstractmethod
    def start_with_preferences(self, preferences: Preferences) -> None:
        """Tells the device to start heating up.

        :param preferences:
            how the user wants the device to be configured.
        """
