from stack import Stack

class StackSpec:
    class A_new_stack:
        def is_empty(self):
            stack = Stack()
            assert stack.depth() == 0
