"""Base class for devices"""

from abc import ABC, abstractmethod

class Device(ABC):
    """Abstraction for a bite healer."""

    @abstractmethod
    def self_test(self) -> None:
        """Tests the device to make sure it is online and
        functional."""

    @abstractmethod
    def start_heating(self) -> None:
        """Tells the device to start heating up."""
