from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_construct_empty():
    obj = SortedFrozenSet([])


def test_construct_from_non_empty_list():
    obj = SortedFrozenSet([2, 1, 3])


def test_construct_from_iterator():
    items = [2, 1, 3, 7]
    iterator = iter(items)
    obj = SortedFrozenSet(iterator)


def test_construct_with_no_args():
    obj = SortedFrozenSet()
