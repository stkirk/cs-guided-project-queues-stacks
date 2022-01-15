"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""

class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

# implement queue functionality (enqueue, dequeue, FIFO) using two stacks
# enqueue process: push onto stack1
# move everything over to stack2 as a way of getting to the bottom(tail) of stack1
# dequeue process: 
    # while stack1 is not empty:
        # value = pop stack 1
        # push value on stack 2
    # pop stack2 as value to return
    # while stack2 is not empty:
        # put everything back in stack1 in right order
        # value = pop stack2
        # push value onto stack1

# FIFO: first in, first out        
class QueueTwoStacks:
    def __init__(self):
        # two stacks: one for on the way in, one for on the way out
        self.in_stack = Stack()
        self.out_stack = Stack()
        
    def enqueue(self, item):
        # add onto in_stack, goes onto end of stack data array
        self.in_stack.push(item)


    def dequeue(self):
        # reverse the main stack by popping every items to the secondary stack
        while len(self.in_stack.data) > 0:
            # pop top element from in_stack and push to out_stack
            top_item = self.in_stack.pop()
            self.out_stack.push(top_item)
        # pop top_item from out_stack, which would have been the bottom of in_stack
        popped_item = self.out_stack.pop()
        # put back in correct order: pop every item from secondary stack back to main stack
        while len(self.out_stack.data) > 0:
            top_item = self.out_stack.pop()
            self.in_stack.push(top_item)

        return popped_item

# Plan: 
# on the way into the queue, enqueue is just like pushing onto a stack
# on the way out of the queue, dequeue needs to "pop" from the bottom of the stack
# to pop from the bottom of a stack we must reverse the stack then pop

# test cases:
q = QueueTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue()) #1
print(q.dequeue()) #2
print(q.dequeue()) #3
q.enqueue(5)
print(q.dequeue()) #4
print(q.dequeue()) #5