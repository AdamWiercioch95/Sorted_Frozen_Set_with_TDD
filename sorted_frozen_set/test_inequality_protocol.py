from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_positive_unequal():
    assert SortedFrozenSet([1, 2, 3]) != SortedFrozenSet([7, 8, 9])


def test_negative_unequal():
    assert not SortedFrozenSet([1, 2, 3]) != SortedFrozenSet([1, 2, 3])


def test_type_mismatch():
    assert SortedFrozenSet([1, 2, 3]) != [1, 2, 3]


def test_identical():
    s = SortedFrozenSet([1, 2, 3])
    assert not s != s
