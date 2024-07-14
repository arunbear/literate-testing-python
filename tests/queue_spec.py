import pytest


class Queue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError()
        self.__capacity = capacity
        self.__queue = []

    def length(self):
        return 0

    def capacity(self):
        return self.__capacity

    def dequeue(self):
        return ()


class QueueSpec:
    class A_new_queue:
        def is_empty(self):
            queue = Queue(1)
            assert queue.length() == 0

        def preserves_positive_bounding_capacity(self):
            capacity = 1
            queue = Queue(capacity)
            assert queue.capacity() == capacity

        def rejects_a_zero_bounding_capacity(self):
            with pytest.raises(ValueError):
                Queue(0)

        def rejects_a_negative_bounding_capacity(self):
            with pytest.raises(ValueError):
                Queue(-1)
    class An_empty_queue:
        def dequeues_an_empty_tuple(self):
            queue = Queue(1)
            assert queue.dequeue() == ()
