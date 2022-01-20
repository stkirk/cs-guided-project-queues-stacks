# Implement queue using deque
'''
Python offers a double-ended queue (deque) to act as a stack/queue. It has some great built-in features:

O(1) appends and pops to both ends of the queue
Implemented using a doubly-linked list
Indexing (new in Python 3.5)
Append (aka push) and pop from both sides of the queue
Reverse in place
Import the deque module and instantiate a shiny new data structure:

from collections import deque

myDeque = deque()
Instant stack implementation:

myDeque.append(val) to push
return myDeque.pop() to pop
Instant queue implementation:

myDeque.append(val) to enqueue
return myDeque.popleft() to dequeue
'''

from collections import deque

class DQueue:
    def __init__(self) -> None:
        self.data = deque()

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.popleft()

q = DQueue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print('q after enqueues-->', q.data)
dequed_item = q.dequeue()
print('dequed_item-->', dequed_item)
print('q after dequeue-->', q.data)
