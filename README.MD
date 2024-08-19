# SortedFrozenSet



`SortedFrozenSet` is a custom immutable data structure that combines the characteristics of a `set` and a `list`, ensuring that elements are unique and sorted. This implementation was created as a learning exercise to explore how to develop custom data structures in Python. The project was built using the principles of Test-Driven Development (TDD) to ensure correctness and reliability.

## Implementation details
The SortedFrozenSet class was designed with the following principles in mind:

 - **Immutability**: The internal storage of elements is done using a tuple, ensuring that the set cannot be altered after creation.
 - **Sorting**: Elements are sorted at the time of creation using Python's built-in sorted() function.
 - **Uniqueness**: The set ensures that all elements are unique, automatically removing any duplicates during initialization. This guarantees that each element appears only once in the set.
 - **Efficiency**: Set operations are implemented using efficient algorithms to minimize time complexity, often leveraging Python’s built-in set data structure.
## Implemented Protocols

The `SortedFrozenSet` class implements several Python protocols to provide a wide range of functionalities:

- **Container Protocol** (`__contains__`): Allows checking if an item is in the set using the `in` keyword.
- **Equality Protocol** (`__eq__`): Supports equality comparison between `SortedFrozenSet` instances.
- **Hashable Protocol** (`__hash__`): Makes `SortedFrozenSet` objects hashable, allowing them to be used as dictionary keys or elements in other sets.
- **Inequality Protocols** (`__lt__`, `__le__`, `__gt__`, `__ge__`): Implements comparison operations to allow for sorting and comparison of sets.
- **Iterable Protocol** (`__iter__`): Allows iteration over elements in the set using a `for` loop.
- **Repr Protocol** (`__repr__`): Provides a string representation of the `SortedFrozenSet` object, useful for debugging.
- **Sequence Protocol** (`__getitem__`, `__len__`): Implements sequence operations, enabling indexing, slicing, and length retrieval.
- **Sized Protocol** (`__len__`): Allows retrieving the number of elements in the set using the `len()` function.

These protocols ensure that `SortedFrozenSet` integrates seamlessly with Python's built-in operations and can be used in a wide variety of contexts.

## Creating a `SortedFrozenSet`

```python
from sorted_frozenset import SortedFrozenSet

# Creating an empty SortedFrozenSet
sfs = SortedFrozenSet()

# Creating a SortedFrozenSet with initial items
sfs = SortedFrozenSet([5, 3, 1, 4, 2, 4, 2, 1])
print(sfs)  # Output: SortedFrozenSet([1, 2, 3, 4, 5])
```


## License
Feel free to use this applications for your private, personal use.
