from collections import deque
from itertools import filterfalse
from typing import Iterator, Generic, TypeVar
from more_itertools import peekable

T = TypeVar('T')

class SequencedCollection(Generic[T]):
    def __init__(self):
        self._collection = deque()

#------------------------------- public accessors -------------------------------
    def add_last(self, item: T) -> None:
        """Add an item to the end of the collection."""
        self._collection.append(item)

    def add_first(self, item: T) -> None:
        """Add an item to the beginning of the collection."""
        self._collection.appendleft(item)
    
    def filtered_stream(self, predicate) -> Iterator[T]:
        """Return a filtered iterator for streaming access to the elements."""
        return filterfalse(predicate, self._collection)

    def get(self, index: int) -> T:
        """Gets an item by its index. """
        return self._collection[index]
    
    def get_first(self) -> T:
        """Get the first item."""
        return self._collection[0]
    
    def get_last(self) -> T:
        """Get the last item."""
        return self._collection[-1]
            
    def is_empty(self) -> bool:
        return len(self._collection) == 0

    def remove(self, item: T) -> None:
        """Remove the first occurrence of an item."""
        self._collection.remove(item)

    def remove_first(self) -> None:
        """Remove the first item."""
        fst = self.get_first()
        self._collection.remove(fst)

    def remove_last(self) -> None:
        """Remove the last item."""
        lst = self.get_last()
        self._collection.remove(lst)

    def reverse(self) -> None:
        """Reverse the order of elements in the collection."""
        self._collection.reverse()

    def stream(self) -> Iterator[T]:
        """Return a peekable iterator for streaming access to the elements."""
        return peekable(self._collection)
    
    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the collection."""
        return iter(self._collection)

    def __len__(self) -> int:
        """Return the number of items in the collection."""
        return len(self._collection)

    def __repr__(self) -> str:
        """Return a string representation of the collection."""
        return f'SequencedCollection({list(self._collection)})'
