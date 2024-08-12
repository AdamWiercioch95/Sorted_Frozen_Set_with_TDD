def is_perfect_length(sequence):
    """
    True if sequence has length 2**n - 1
    otherwise False
    """
    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)


class LevelOrderIterator:
    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._index = 0

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent a perfect binary tree with length 2 ** n - 1")

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration

        result = self._sequence[self._index]
        self._index += 1

        return result


def left_child(index):
    return 2 * index + 1


def right_child(index):
    return 2 * index + 2


class PreorderIterator:
    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._stack = [0]

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent a perfect binary tree with length 2 ** n - 1")

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        idx = self._stack.pop()
        result = self._sequence[idx]

        right_child_index = right_child(idx)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = left_child(idx)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result


class InorderIterator:
    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._stack = []
        self._index = 0

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent a perfect binary tree with length 2 ** n - 1")

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0 and self._index >= len(self._sequence):
            raise StopIteration

        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = left_child(self._index)

        index = self._stack.pop()
        result = self._sequence[index]
        self._index = right_child(index)

        return result


tree = ['*', '+', '-', 'a', 'b', 'c', 'd']
iterator = InorderIterator(tree)
' '.join(iterator)
