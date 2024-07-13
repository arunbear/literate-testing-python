import pytest

from stack import Stack

class StackSpec:
    class A_new_stack:
        def is_empty(self):
            stack = Stack()
            assert stack.depth() == 0

    class An_empty_stack:
        def throws_when_queried_for_its_top_item(self):
            with pytest.raises(Stack.InvalidStateError):
                stack = Stack()
                stack.top()
