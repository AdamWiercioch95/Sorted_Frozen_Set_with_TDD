from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_equal_sets_have_the_same_hash_code():
    assert hash(SortedFrozenSet([1, 2, 3])) == hash(SortedFrozenSet([1, 2, 3]))


def test_unequal_sets_have_different_hash_code():
    assert hash(SortedFrozenSet([1, 2, 3])) != hash(SortedFrozenSet([4, 5, 6]))
