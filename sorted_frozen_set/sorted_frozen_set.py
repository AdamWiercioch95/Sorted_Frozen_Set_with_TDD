from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain


class SortedFrozenSet(Sequence):
    def __init__(self, items=None):
        self._items = tuple(sorted(set(items) if items is not None else set()))

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedFrozenSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return f'{type(self).__name__}({list(self._items) or ""})'

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._items == other._items

    def __hash__(self):
        return hash((type(self), self._items))

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return SortedFrozenSet(self._items + other._items)

    def __mul__(self, other):
        return self if other > 0 else SortedFrozenSet()

    def __rmul__(self, other):
        return self * other

    def count(self, item):
        return int((item in self))

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError(f'{item!r} not found')

    def isdisjoint(self, iterable):
        return not len(self & SortedFrozenSet(iterable))

    def issubset(self, iterable):
        return self <= SortedFrozenSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedFrozenSet(iterable)

    def intersection(self, iterable):
        return self & SortedFrozenSet(iterable)

    def union(self, iterable):
        return self | SortedFrozenSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedFrozenSet(iterable)

    def difference(self, iterable):
        return self - SortedFrozenSet(iterable)

    def __lt__(self, iterable):
        return self <= iterable and len(self) < len(iterable)

    def __le__(self, iterable):
        for item in self._items:
            if item not in iterable:
                return False

        return True

    def __and__(self, iterable):
        temp = set()

        for item in self._items:
            if item in iterable:
                temp.add(item)

        return SortedFrozenSet(temp)

    def __or__(self, iterable):
        return SortedFrozenSet(chain(self, iterable))

    def __xor__(self, iterable):
        return (self | iterable) - (self & iterable)

    def __sub__(self, iterable):
        temp = set()

        for item in self:
            if item not in iterable:
                temp.add(item)

        return SortedFrozenSet(temp)
