class Queue:
    def __init__(self):
        self.__queue = []

    def length(self):
        return 0


class QueueSpec:
    class A_new_queue:
        def is_empty(self):
            queue = Queue()
            assert queue.length() == 0
