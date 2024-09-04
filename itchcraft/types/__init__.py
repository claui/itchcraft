"""Types used in several places"""

from abc import ABC, abstractmethod
from collections.abc import Collection
from typing import Union

from ..prefs import Preferences


SizedPayload = Union[bytes, Collection[int]]


class BiteHealer(ABC):
    """Abstraction for a bite healer."""

    @abstractmethod
    def self_test(self) -> None:
        """Tests the device to make sure it is online and
        functional."""

    @abstractmethod
    def start_with_preferences(self, preferences: Preferences) -> None:
        """Tells the device to start heating up."""
