from collections.abc import Sequence


class SortedFrozenSet(Sequence):
    def __init__(self, items=None):
        self._items = sorted(set(items) if items is not None else set())

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedFrozenSet(result) if isinstance(index, slice) else result

    def __eq__(self, other):
        return self._items == other._items

    # def count(self, item):
        # return 1 if value in self._items else 0
        # return self._items.count(item)
