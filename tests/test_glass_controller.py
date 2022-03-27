"""Test cases for glass_controller.py"""

from unittest.mock import MagicMock
import pytest
from src.glass_controller import GlassController


@pytest.fixture
def test_objects():
    return [
        GlassController(0, 0, 0),
        GlassController(1, 1, 2),
        GlassController(50, 40, 100),
    ]


def test_init_glass_controller(test_objects):
    expected = {
        "rows": [0, 1, 50],
        "cols": [0, 1, 40],
        "volumes": [0, 2, 100],
    }
    assert [obj.row for obj in test_objects] == expected["rows"]
    assert [obj.col for obj in test_objects] == expected["cols"]
    assert [obj.volume for obj in test_objects] == expected["volumes"]
    assert [obj.glasses for obj in test_objects]


def test_initialize_glasses(test_objects):
    obj = test_objects.pop()
    obj._get_number_of_glasses = MagicMock(return_value=2)
    assert len(obj._initialize_glasses()) == 2


def test_get_number_of_glasses(test_objects):
    expected = [1, 3, 1326]
    actual = [obj._get_number_of_glasses() for obj in test_objects]
    assert actual == expected


def test_get_glass_idx(test_objects):
    expected = [0, 2, 1315]
    actual = [obj._get_glass_idx() for obj in test_objects]
    assert actual == expected


def test_run(test_objects):
    actual = [obj.run() for obj in test_objects]
    expected = [0, 0.25, 0]
    assert [res[1] for res in actual] == expected
