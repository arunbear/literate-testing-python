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

        def throws_when_popped(self):
            with pytest.raises(Stack.InvalidStateError):
                stack = Stack()
                stack.pop()

        def acquires_depth_by_retaining_a_pushed_item_as_its_top(self):
            # given ->
            stack = Stack()

            # when ->
            rock = "rock"
            stack.push(rock)

            # then ->
            assert stack.depth() == 1
            assert stack.top() == rock

    class A_non_empty_stack:
        def becomes_deeper_by_retaining_a_pushed_item_as_its_top(self):
            # given ->
            stack = Stack()
            stack.push("paper")
            old_depth = stack.depth()

            # when ->
            rock = "rock"
            stack.push(rock)

            # then ->
            assert stack.depth() > old_depth
            assert stack.top() == rock
