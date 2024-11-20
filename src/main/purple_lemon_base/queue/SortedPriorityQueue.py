from purple_lemon_base.list.positional_list_base import PositionalListBase
from purple_lemon_base.queue import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalListBase()