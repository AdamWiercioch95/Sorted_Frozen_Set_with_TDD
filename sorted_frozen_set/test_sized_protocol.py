from collections.abc import Sized

from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_empty_with_default():
    s = SortedFrozenSet()
    assert len(s) == 0


def test_empty():
    s = SortedFrozenSet([])
    assert len(s) == 0


def test_one():
    s = SortedFrozenSet([42])
    assert len(s) == 1


def test_ten():
    s = SortedFrozenSet(range(10))
    assert len(s) == 10


def test_with_duplicates():
    s = SortedFrozenSet([6, 6, 6])
    assert len(s) == 1


def test_sized_protocol():
    assert issubclass(SortedFrozenSet, Sized)
