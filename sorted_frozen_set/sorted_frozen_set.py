from collections.abc import Sequence


class SortedFrozenSet(Sequence):
    def __init__(self, items=None):
        self._items = tuple(sorted(set(items) if items is not None else set()))

    def __contains__(self, item):
        return item in self._items

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
