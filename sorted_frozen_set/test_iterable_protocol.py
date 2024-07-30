import pytest

from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_iter():
    s = SortedFrozenSet([7, 2, 1, 1, 9])
    s_iter = iter(s)
    assert next(s_iter) == 1
    assert next(s_iter) == 2
    assert next(s_iter) == 7
    assert next(s_iter) == 9
    with pytest.raises(StopIteration):
        next(s_iter)


def test_for_loop():
    s = SortedFrozenSet([7, 2, 1, 1, 9])
    expected = [1, 2, 7, 9]
    counter = 0
    for item in s:
        assert item == expected[counter]
        counter += 1
