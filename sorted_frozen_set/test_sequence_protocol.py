import pytest

from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


@pytest.fixture
def s_sequence():
    return SortedFrozenSet([1, 4, 9, 13, 15])


def test_index_zero(s_sequence):
    assert s_sequence[0] == 1


def test_index_four(s_sequence):
    assert s_sequence[4] == 15


def test_index_one_beyond_the_end(s_sequence):
    with pytest.raises(IndexError):
        item = s_sequence[5]


def test_index_minus_one(s_sequence):
    assert s_sequence[-1] == 15


def test_index_minus_five(s_sequence):
    assert s_sequence[-5] == 1


def test_index_one_before_beginning(s_sequence):
    with pytest.raises(IndexError):
        item = s_sequence[-6]


def test_slice_from_start(s_sequence):
    assert s_sequence[:3] == SortedFrozenSet([1, 4, 9])


def test_slice_to_end(s_sequence):
    assert s_sequence[3:] == SortedFrozenSet([13, 15])


def test_slice_empty(s_sequence):
    assert s_sequence[7:10] == SortedFrozenSet()


def test_slice_arbitrary(s_sequence):
    assert s_sequence[2:4] == SortedFrozenSet([9, 13])


def test_slice_step(s_sequence):
    assert s_sequence[0:5:2] == SortedFrozenSet([1, 9, 15])


def test_slice_full(s_sequence):
    assert s_sequence[:] == s_sequence


def test_count_zero(s_sequence):
    assert s_sequence.count(10) == 0


def test_count_four(s_sequence):
    assert s_sequence.count(4) == 1


def test_index_positive(s_sequence):
    assert s_sequence.index(4) == 1


def test_index_negative(s_sequence):
    with pytest.raises(ValueError):
        s_sequence.index(5)


def test_reversed(s_sequence):
    r = reversed(s_sequence)
    assert next(r) == 15
    assert next(r) == 13
    assert next(r) == 9
    assert next(r) == 4
    assert next(r) == 1
    with pytest.raises(StopIteration):
        next(r)
