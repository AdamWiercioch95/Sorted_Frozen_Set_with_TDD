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
