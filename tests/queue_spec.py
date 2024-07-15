import pytest
from optional import Optional, Something


class Queue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError()
        self.__capacity = capacity
        self.__queue = []

    def length(self):
        return len(self.__queue)

    def capacity(self):
        return self.__capacity

    def dequeue(self):
        if self.length() == 0:
            return Optional.empty()
        else:
            return Something(self.__queue.pop(0))

    def enqueue(self, item):
        if len(self.__queue) < self.__capacity:
            self.__queue.append(item)


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
        def dequeues_an_empty_optional(self):
            queue = Queue(1)
            assert queue.dequeue() == Optional.empty()

        def becomes_non_empty_when_value_enqueued(self):
            queue = Queue(1)
            queue.enqueue('rock')
            assert queue.length() > 0

    class A_non_empty_queue:
        class that_is_not_full:
            def becomes_longer_when_value_enqueued(self):
                # given ->
                queue = Queue(2)
                queue.enqueue('rock')
                old_length = queue.length()

                # when ->
                queue.enqueue('paper')

                # then ->
                assert queue.length() > old_length

            def becomes_full_when_enqueued_up_to_capacity(self):
                # given ->
                queue = Queue(2)
                queue.enqueue('rock')

                # when ->
                queue.enqueue('paper')

                # then ->
                assert queue.length() == queue.capacity()

        class that_is_full:
            def ignores_further_enqueued_values(self):
                # given ->
                queue = Queue(1)
                queue.enqueue('rock')

                # when ->
                queue.enqueue('paper')

                # then ->
                assert queue.length() == 1
                assert queue.dequeue() == Something('rock')

            def becomes_non_full_when_dequeued(self):
                # given ->
                queue = Queue(1)
                queue.enqueue('rock')

                # when ->
                queue.dequeue()

                # then ->
                assert queue.length() < queue.capacity()
