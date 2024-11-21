import pytest
from main.purple_lemon_base.deque.Sequenced_Collection import SequencedCollection

@pytest.fixture
def sq_example():
    seq_col = SequencedCollection()
    seq_col._collection.extend([0,1,2,3,4,5])
    return seq_col

def test_add_first():
    seq_col = SequencedCollection()
    seq_col.add_first(2)
    seq_col.add_first(1)
    assert list(seq_col._collection) == [1, 2]
    assert next(seq_col.__iter__()) == 1

def test_add_last():
    seq_col = SequencedCollection()
    seq_col.add_first(1)
    seq_col.add_last(0)
    seq_col.add_last(2)
    assert list(seq_col._collection) == [1, 0, 2]
    assert next(seq_col.__iter__()) == 1

def test_get(sq_example):
    assert sq_example.get(0) == 0
    assert sq_example.get(1) == 1

def test_remove(sq_example):
    seq_col = SequencedCollection()
    seq_col.add_first(1)
    seq_col.add_last(2)
    seq_col.remove(1)
    assert list(seq_col._collection) == [2]
    assert seq_col.get_first() == 2

def test_reverse():
    seq_col = SequencedCollection()
    seq_col.add_first(1)
    seq_col.add_last(2)
    seq_col.reverse()
    assert list(seq_col._collection) == [2, 1]
    assert seq_col.get_first() == 2

def test_stream():
    seq_col = SequencedCollection()
    seq_col.add_first(1)
    seq_col.add_last(2)
    stream_iterator = seq_col.stream()
    assert list(stream_iterator) == [1, 2]


def test_is_empty():
    seq_col = SequencedCollection()
    assert seq_col.is_empty() 

def test_len():
    seq_col = SequencedCollection()
    seq_col.add_first(1)
    seq_col.add_first(2)
    assert len(seq_col) == 2
    seq_col.remove(1)
    assert len(seq_col) == 1

def test_repr():
    seq_col = SequencedCollection()
    seq_col.add_first(1)
    seq_col.add_last(2)
    assert repr(seq_col) == "SequencedCollection([1, 2])"

if __name__ == "__main__":
    pytest.main()

