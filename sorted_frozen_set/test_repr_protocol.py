from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_repr_empty():
    s = SortedFrozenSet([])
    assert repr(s) == 'SortedFrozenSet()'


def test_repr_non_empty():
    s = SortedFrozenSet([2, 1, 3, 7])
    assert repr(s) == 'SortedFrozenSet([1, 2, 3, 7])'


def test_repr_with_no_args():
    s = SortedFrozenSet()
    assert repr(s) == 'SortedFrozenSet()'
