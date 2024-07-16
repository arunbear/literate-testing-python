# Literate Testing
These are examples of how to use naming conventions and grouping to write unit tests in a highly readable manner,
resembling a specification so that the reader may more easily gain an understanding of the code being tested.

The examples here are fleshed out and runnable versions based on those described in the talk "Structure and Interpretation of Test Cases" by Kevlin Henney

The tests and code are also developed [incrementally](https://github.com/arunbear/literate-testing-python/commits/main/) following the Test Driven Development approach.

## Examples

[Leap year testing](https://github.com/arunbear/literate-testing-python/blob/main/tests/leapyear_spec.py)

[Stacks](https://github.com/arunbear/literate-testing-python/blob/main/tests/stack_spec.py)

[Queues](https://github.com/arunbear/literate-testing-python/blob/main/tests/queue_spec.py)

See below for [test output](#test-output)

## See Also

[Structure and Interpretation of Test Cases](https://www.youtube.com/watch?v=tWn8RA_DEic)

[Stylish Unit Tests](https://capgemini.github.io/development/unit-test-structure/)

## Test Output

```
% pytest -v

============================= test session starts ==============================
platform linux -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0 -- /home/me/PycharmProjects/literate-testing-python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/me/PycharmProjects/literate-testing-python
configfile: pytest.ini
testpaths: tests
plugins: relaxed-2.0.2
collecting ... collected 38 items

LeapYearSpec

    A year is a leap year

        if it is divisible by 4 but not by 100[2004]
        if it is divisible by 4 but not by 100[1984]
        if it is divisible by 4 but not by 100[4]
        if it is divisible by 400[2000]
        if it is divisible by 400[1600]
        if it is divisible by 400[400]

    A year is not a leap year

        if it is not divisible by 4[2022]
        if it is not divisible by 4[2019]
        if it is not divisible by 4[1999]
        if it is not divisible by 4[1]
        if it is divisible by 100 but not by 400[2100]
        if it is divisible by 100 but not by 400[1900]
        if it is divisible by 100 but not by 400[100]

    A year is supported

        if it is positive[1]
        if it is positive[100]

    A year is not supported

        if it is zero
        if it is nagative[-1]
        if it is nagative[-4]
        if it is nagative[-100]
        if it is nagative[-400]

QueueSpec

    A new queue

        is empty
        preserves positive bounding capacity
        rejects a zero bounding capacity
        rejects a negative bounding capacity

    An empty queue

        dequeues an empty optional
        becomes non empty when value enqueued

    A non empty queue

        that is not full

            becomes longer when value enqueued
            becomes full when enqueued up to capacity

        that is full

            ignores further enqueued values
            becomes non full when dequeued
        becomes shorter when dequeued
        dequeues values in order enqueued

StackSpec

    A new stack

        is empty

    An empty stack

        throws when queried for its top item
        throws when popped
        acquires depth by retaining a pushed item as its top

    A non empty stack

        becomes deeper by retaining a pushed item as its top
        on popping reveals tops in reverse order of pushing

============================== 38 passed in 0.08s ==============================
```
