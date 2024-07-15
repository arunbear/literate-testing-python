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
