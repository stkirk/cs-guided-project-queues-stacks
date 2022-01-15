"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]
# In this array implementation of a stack, the item at the end of the array is the "top" of the stack

# Plan:
# use two stacks, one for the values in order and the other for successive max values as new items are added and the max value is "leapfrogged"
# when pushing a new value onto the stack, also push a nex max onto the maximums stack if the new value is greater than or equal to the current maximum
# edge case: duplicate values--> when popping, if the value is the same as the value at the top of the maximums sack, also pop from the maximums stack
# note: if second largest value is added to the main stack after the largest value it will always be popped from the list before the largest can be popped, therefore we don't have to worry about saving it in max stack


class MaxStack:
    def __init__(self):
        # init a stack with all the items
        self.stack = Stack()
        # also init a stack to keep track of the max element in the first stack
        self.maximums_stack = Stack()


    def push(self, item):
        """Add a new item onto the top of our main stack."""
        # every new item is added to the main stack
        self.stack.push(item)
        # assign current max to a variable even if it is None
        current_max = self.maximums_stack.peek()

        # check if current max in max stack is None or if new item is bigger than the item at the top of maximums_stack
        if current_max is None or item >= current_max:
            self.maximums_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        # save item being popped
        top_of_stack = self.stack.pop()
        # peek at both stacks to see if the item being popped is our maximum
        if top_of_stack == self.maximums_stack.peek():
            # its the max, pop it off the max stack too
            self.maximums_stack.pop()

        return top_of_stack


    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        # show only
        return self.maximums_stack.peek()

# test cases
myStack = MaxStack()
myStack.push(1)
myStack.push(74)
myStack.push(36)
print(myStack.get_max()) # 74
print(myStack.pop()) #36
myStack.push(74)
myStack.push(10) # 1, 74, 74, 10 at this point
print(myStack.get_max()) # 74
print(myStack.pop()) # 10
print(myStack.pop()) # 74
print(myStack.get_max()) # 74

# expected: 74, 36, 74, 10, 74, 74
