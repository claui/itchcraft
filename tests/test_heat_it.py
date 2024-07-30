# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring

from collections.abc import Callable, Iterator
from contextlib import (
    AbstractContextManager,
    nullcontext,
)
from dataclasses import asdict
from typing import Optional, Union
from unittest.mock import ANY

import pytest
import pytest_mock

from itchcraft import Api, devices
from itchcraft.api import StartParams
from itchcraft.backend import BulkTransferDevice
from itchcraft.device import Device
from itchcraft.heat_it import HeatItDevice
from itchcraft.prefs import Duration, Generation, SkinSensitivity


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


def test_no_preferences(bulk_transfer: pytest_mock.MockType) -> None:
    Api().start()
    bulk_transfer.assert_called_with(
        ANY, [0xFF, 0x08, 0x00, 0x00, 0x08]
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(),
        StartParams(duration='short'),
        StartParams(duration=Duration.SHORT),
        StartParams(duration='short', generation='child'),
        StartParams(
            duration=Duration.SHORT, generation=Generation.CHILD
        ),
        StartParams(generation='child'),
        StartParams(generation=Generation.CHILD),
        StartParams(duration=Duration.SHORT),
        StartParams(duration='short', skin_sensitivity='sensitive'),
        StartParams(
            duration=Duration.SHORT,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
        StartParams(skin_sensitivity='sensitive'),
        StartParams(skin_sensitivity=SkinSensitivity.SENSITIVE),
        StartParams(
            duration='short',
            generation='child',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation='child',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.CHILD,
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.CHILD,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
    ],
)
def test_child_sensitive_short(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x00, 0x00, 0x08],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='medium'),
        StartParams(duration=Duration.MEDIUM),
        StartParams(duration='medium', generation='child'),
        StartParams(
            duration=Duration.MEDIUM, generation=Generation.CHILD
        ),
        StartParams(duration='medium', skin_sensitivity='sensitive'),
        StartParams(
            duration=Duration.MEDIUM,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
        StartParams(
            duration='medium',
            generation='child',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation='child',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.CHILD,
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.CHILD,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
    ],
)
def test_child_sensitive_medium(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x00, 0x01, 0x09],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='long'),
        StartParams(duration=Duration.LONG),
        StartParams(duration='long', generation='child'),
        StartParams(
            duration=Duration.LONG, generation=Generation.CHILD
        ),
        StartParams(duration='long', skin_sensitivity='sensitive'),
        StartParams(
            duration=Duration.LONG,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
        StartParams(
            duration='long',
            generation='child',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.LONG,
            generation='child',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.CHILD,
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.CHILD,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
    ],
)
def test_child_sensitive_long(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x00, 0x02, 0x0A],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='short', generation='adult'),
        StartParams(
            duration=Duration.SHORT, generation=Generation.ADULT
        ),
        StartParams(generation='adult'),
        StartParams(generation=Generation.ADULT),
        StartParams(
            duration='short',
            generation='adult',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation='adult',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.ADULT,
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
    ],
)
def test_adult_sensitive_short(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x02, 0x00, 0x0A],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='medium', generation='adult'),
        StartParams(
            duration=Duration.MEDIUM, generation=Generation.ADULT
        ),
        StartParams(
            duration='medium',
            generation='adult',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation='adult',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.ADULT,
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
    ],
)
def test_adult_sensitive_medium(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x02, 0x01, 0x0B],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='long', generation='adult'),
        StartParams(
            duration=Duration.LONG, generation=Generation.ADULT
        ),
        StartParams(
            duration='long',
            generation='adult',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.LONG,
            generation='adult',
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.ADULT,
            skin_sensitivity='sensitive',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.SENSITIVE,
        ),
    ],
)
def test_adult_sensitive_long(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x02, 0x02, 0x0C],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='short', skin_sensitivity='regular'),
        StartParams(
            duration=Duration.SHORT,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
        StartParams(skin_sensitivity='regular'),
        StartParams(skin_sensitivity=SkinSensitivity.REGULAR),
        StartParams(
            duration='short',
            generation='child',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation='child',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.CHILD,
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.CHILD,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
    ],
)
def test_child_regular_short(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x01, 0x00, 0x09],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='medium', skin_sensitivity='regular'),
        StartParams(
            duration=Duration.MEDIUM,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
        StartParams(
            duration='medium',
            generation='child',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation='child',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.CHILD,
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.CHILD,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
    ],
)
def test_child_regular_medium(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x01, 0x01, 0x0A],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(duration='long', skin_sensitivity='regular'),
        StartParams(
            duration=Duration.LONG,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
        StartParams(
            duration='long',
            generation='child',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.LONG,
            generation='child',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.CHILD,
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.CHILD,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
    ],
)
def test_child_regular_long(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x01, 0x02, 0x0B],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(generation='adult', skin_sensitivity='regular'),
        StartParams(
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
        StartParams(
            duration='short',
            generation='adult',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation='adult',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.ADULT,
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.SHORT,
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
    ],
)
def test_adult_regular_short(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x03, 0x00, 0x0B],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(
            duration='medium',
            generation='adult',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation='adult',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.ADULT,
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.MEDIUM,
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
    ],
)
def test_adult_regular_medium(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x03, 0x01, 0x0C],
    )


@pytest.mark.parametrize(
    'preferences',
    [
        StartParams(
            duration='long',
            generation='adult',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.LONG,
            generation='adult',
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.ADULT,
            skin_sensitivity='regular',
        ),
        StartParams(
            duration=Duration.LONG,
            generation=Generation.ADULT,
            skin_sensitivity=SkinSensitivity.REGULAR,
        ),
    ],
)
def test_adult_regular_long(
    bulk_transfer: pytest_mock.MockType,
    preferences: StartParams,
) -> None:
    Api().start(**asdict(preferences))
    bulk_transfer.assert_called_with(
        ANY,
        [0xFF, 0x08, 0x03, 0x02, 0x0D],
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
