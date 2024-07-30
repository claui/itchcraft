# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring

from collections.abc import Callable, Iterator
from contextlib import (
    AbstractContextManager,
    nullcontext,
)
from typing import Optional, Union
from unittest.mock import ANY

import pytest
import pytest_mock

from itchcraft import Api, devices
from itchcraft.backend import BulkTransferDevice
from itchcraft.device import Device
from itchcraft.heat_it import HeatItDevice


@pytest.fixture(name='dummy_device')
def fixture_dummy_device() -> AbstractContextManager[Device]:
    return nullcontext(HeatItDevice(_DummyUsbBulkTransferDevice()))


@pytest.fixture(name='find_dummy_device')
def fixture_find_dummy_device(
    dummy_device: AbstractContextManager[Device],
) -> Callable[[], Iterator[AbstractContextManager[Device]]]:
    return lambda: iter((dummy_device,))


@pytest.fixture(name='bulk_transfer')
def fixture_bulk_transfer(
    mocker: pytest_mock.MockerFixture,
    monkeypatch: pytest.MonkeyPatch,
    find_dummy_device: Iterator[AbstractContextManager[Device]],
) -> Iterator[pytest_mock.MockType]:
    monkeypatch.setattr(devices, 'find_devices', find_dummy_device)
    bulk_transfer = mocker.spy(
        _DummyUsbBulkTransferDevice, 'bulk_transfer'
    )
    yield bulk_transfer
    assert bulk_transfer.call_count == 3


def test_default(bulk_transfer: pytest_mock.MockType) -> None:
    Api().start()
    bulk_transfer.assert_called_with(
        ANY, [0xFF, 0x08, 0x00, 0x00, 0x08]
    )


class _DummyUsbBulkTransferDevice(BulkTransferDevice):
    def bulk_transfer(
        self, request: Union[list[int], bytes, bytearray]
    ) -> bytes:
        return b'123456789012'

    @property
    def product_name(self) -> Optional[str]:
        return 'dummy'

    @property
    def serial_number(self) -> Optional[str]:
        return None

    def __str__(self) -> str:
        return 'dummy device for testing purposes'
