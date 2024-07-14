class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def length(self):
        return 0

    def capacity(self):
        return self.__capacity


class QueueSpec:
    class A_new_queue:
        def is_empty(self):
            queue = Queue(1)
            assert queue.length() == 0

        def preserves_positive_bounding_capacity(self):
            capacity = 1
            queue = Queue(capacity)
            assert queue.capacity() == capacity
