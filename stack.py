class Stack:
    class InvalidStateError(Exception):
        pass

    def __init__(self):
        self.__stack = []

    def depth(self):
        return len(self.__stack)

    def top(self):
        if len(self.__stack) == 0:
            raise Stack.InvalidStateError

        return self.__stack[-1]

    def pop(self):
        if len(self.__stack) == 0:
            raise Stack.InvalidStateError

        self.__stack.pop()

    def push(self, item):
        self.__stack.append(item)
