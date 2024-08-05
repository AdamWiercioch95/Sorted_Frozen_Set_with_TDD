from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_positive_equal():
    s1 = SortedFrozenSet([4, 5, 6])
    s2 = SortedFrozenSet([6, 4, 5])
    assert s1 == s2


def test_negative_equal():
    s1 = SortedFrozenSet([4, 5, 6])
    s2 = SortedFrozenSet([7, 4, 5])
    assert not s1 == s2


def test_type_mismatch():
    s = SortedFrozenSet([4, 5, 6])
    l = [4, 5, 6]
    assert not s == l


def test_identical():
    s = SortedFrozenSet([4, 5, 6])
    assert s == s
