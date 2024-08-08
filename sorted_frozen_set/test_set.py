from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_lt_positive():
    s1 = SortedFrozenSet({1, 2})
    s2 = SortedFrozenSet({1, 2, 3})
    assert s1 < s2


def test_lt_negative():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({1, 2, 3})
    assert not s1 < s2


def test_lte_positive():
    s1 = SortedFrozenSet({1, 2})
    s2 = SortedFrozenSet({1, 2, 3})
    assert s1 <= s2


def test_lte_negative():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({1, 2})
    assert not s1 <= s2


def test_gt_positive():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({1, 2})
    assert s1 > s2


def test_gt_negative():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({1, 2, 3})
    assert not s1 > s2


def test_gte_positive():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({1, 2})
    assert s1 >= s2


def test_gte_negative():
    s1 = SortedFrozenSet({1, 2})
    s2 = SortedFrozenSet({1, 2, 3})
    assert not s1 >= s2


def test_issubset_proper_positive():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [1, 2, 3]
    assert s1.issubset(s2)


def test_issubset_proper_negative():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [1, 2]
    assert not s1.issubset(s2)


def test_issuperset_proper_positive():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [1, 2]
    assert s1.issuperset(s2)


def test_issuperset_proper_negative():
    s1 = SortedFrozenSet({1, 2})
    s2 = [1, 2, 3]
    assert not s1.issuperset(s2)


def test_isdisjoint_proper_positive():
    s1 = SortedFrozenSet({1, 2})
    s2 = [3, 4]
    assert s1.isdisjoint(s2)


def test_isdisjoint_proper_negative():
    s1 = SortedFrozenSet({1, 2})
    s2 = [2, 3]
    assert not s1.isdisjoint(s2)


def test_intersection_operation():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({3, 4, 5})
    assert s1 & s2 == SortedFrozenSet({3})


def test_union_operation():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({3, 4, 5})
    assert s1 | s2 == SortedFrozenSet({1, 2, 3, 4, 5})


def test_symmetric_difference_operation():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({3, 4, 5})
    assert s1 ^ s2 == SortedFrozenSet({1, 2, 4, 5})


def test_difference_operation():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = SortedFrozenSet({3, 4, 5})
    assert s1 - s2 == SortedFrozenSet({1, 2})


def test_intersection_method():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [3, 4, 5]
    assert s1.intersection(s2) == SortedFrozenSet({3})


def test_union_method():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [3, 4, 5]
    assert s1.union(s2) == SortedFrozenSet({1, 2, 3, 4, 5})


def test_symmetric_difference_method():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [3, 4, 5]
    assert s1.symmetric_difference(s2) == SortedFrozenSet({1, 2, 4, 5})


def test_difference_method():
    s1 = SortedFrozenSet({1, 2, 3})
    s2 = [3, 4, 5]
    assert s1.difference(s2) == SortedFrozenSet({1, 2})
