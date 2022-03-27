"""Test cases for glass.py"""

import os
import pytest
import mock
from src.glass import Glass


@pytest.fixture
def test_object():
    return Glass()


def test_init_glass_default(test_object):
    assert test_object.volume == 0
    assert test_object.overflow == 0
    assert test_object.limit == 0.25


@mock.patch.dict(os.environ, {"LIMIT": "1"})
def test_init_glass_custom_limit():
    obj = Glass(float(os.environ["LIMIT"]))
    assert obj.volume == 0
    assert obj.overflow == 0
    assert obj.limit == 1


@pytest.mark.parametrize(
    "in_volume, out_volume, out_overflow",
    [(0, 0, 0), (0.25, 0.25, 0), (500, 0.25, 499.75)],
)
def test_pour_valid(test_object, in_volume, out_volume, out_overflow):
    test_object.pour(in_volume)
    assert test_object.volume == out_volume
    assert test_object.overflow == out_overflow


@pytest.mark.parametrize("volume", [None, -1])
def test_pour_invalid(test_object, volume):
    with pytest.raises(ValueError):
        test_object.pour(volume)
