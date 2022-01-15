# Queues: first-in first-out, FIFO
# Think of the line at the bank
# Operations on a queue:
    # ENQUEUE: add item to end of the line
    # DEQUEUE: take item from the front of the line

# stock ListNode:
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<ListNode({self.value})>"

class Queue:
    def __init__(self):
        # keep track of head and tail this time, both initialized to None
        # head and tail start off both pointing to None
        self.head = self.tail = None

    # override the __str__ method, which is used to print
    # print something like this: (1)->(2)->(3)
    def __str__(self) -> str:
        lst_str = []
        current_node = self.head
        while current_node is not None:
            lst_str.append(f"({current_node.value})")
            current_node = current_node.next

        return "->".join(lst_str)

    # append new_node to end of the line (tail)
    def enqueue(self, new_node):
        # special case: enqueueing to empty list
        if self.head is None:
            self.head = self.tail = new_node
            return

        # general case    
        self.tail.next = new_node
        self.tail = self.tail.next # could just be new_node???
    
    # pop item from front of line (head)
    def dequeue(self):
        # save old_head, its what we want to return
        old_head = self.head
        # set head to next in line
        self.head = self.head.next
        # delete old_head's link to the list
        old_head.next = None
        # check if list is empty after dequeueing
        if self.head is None:
            # need to also reset the tail pointer to initial state
            self.tail = None
        # return the node that was at the front
        return old_head

q = Queue()

q.enqueue(ListNode(1))
q.enqueue(ListNode(2))
q.enqueue(ListNode(3))
q.enqueue(ListNode(4))

print('current queue-->', q)

print('dequeue-->', q.dequeue())
print('dequeue-->', q.dequeue())

print('after dequeue-->', q)

