# Implement queue using deque

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
