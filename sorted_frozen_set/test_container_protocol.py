from collections.abc import Container

import pytest

from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


@pytest.fixture
def sorted_frozen_set():
    return SortedFrozenSet([6, 7, 3, 9])


def test_positive_contained(sorted_frozen_set):
    assert 6 in sorted_frozen_set


def test_negative_contained(sorted_frozen_set):
    assert not (1 in sorted_frozen_set)


def test_positive_not_contained(sorted_frozen_set):
    assert 1 not in sorted_frozen_set


def test_negative_not_contained(sorted_frozen_set):
    assert not (6 not in sorted_frozen_set)


def test_container_protocol():
    assert issubclass(SortedFrozenSet, Container)
