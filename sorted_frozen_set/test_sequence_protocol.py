from collections.abc import Sequence

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


def test_add_disjoint():
    s1 = SortedFrozenSet([1, 2, 3])
    s2 = SortedFrozenSet([4, 5, 6])
    assert s1 + s2 == SortedFrozenSet([1, 2, 3, 4, 5, 6])


def test_add_equal():
    s = SortedFrozenSet([1, 2, 3])
    assert s + s == s


def test_add_intersecting():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([4, 5, 6])
    assert s + t == SortedFrozenSet([1, 2, 3, 4, 5, 6])


def test_add_type_error_left():
    s = SortedFrozenSet([1, 2, 3])
    t = (4, 5, 6)
    with pytest.raises(TypeError):
        _ = s + t


def test_add_type_error_right():
    s = (4, 5, 6)
    t = SortedFrozenSet([1, 2, 3])
    with pytest.raises(TypeError):
        _ = s + t


def test_repetition_zero_right():
    s = SortedFrozenSet([1, 2, 3])
    assert s * 0 == SortedFrozenSet()


def test_repetition_negative_right():
    s = SortedFrozenSet([1, 2, 3])
    assert s * -5 == SortedFrozenSet()


def test_repetition_nonzero_right():
    s = SortedFrozenSet([1, 2, 3])
    assert s * 42 == SortedFrozenSet([1, 2, 3])


def test_repetition_zero_left():
    s = SortedFrozenSet([1, 2, 3])
    assert 0 * s == SortedFrozenSet()


def test_repetition_negative_left():
    s = SortedFrozenSet([1, 2, 3])
    assert -5 * s == SortedFrozenSet()


def test_repetition_nonzero_left():
    s = SortedFrozenSet([1, 2, 3])
    assert 42 * s == SortedFrozenSet([1, 2, 3])


def test_sequence_protocol():
    assert issubclass(SortedFrozenSet, Sequence)
