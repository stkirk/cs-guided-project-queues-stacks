# implement a queue using two stacks in the exisitng code:

# existing Stack class uses list to store items. Its two operations are to append(push) items to the end of the array and to pop items off of the end of the array and return them
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# parameter requests is a list of commands to push a value or pop a value
# commands should be performed in order
# stacks and queues share the same operation to add to top
def solution(requests):
    # incoming, append to this stack last item added becomes "back of line"
    left = Stack()
    # outgoing: transfer left stack here to pop from "front of line"
    right = Stack()

    def insert(x):
        # insert to the left stack
        left.push(x)
        

    def remove():
        # possible safety check for empty stack?
        if left.isEmpty():
            return None
        # pop all items in left and append them to right
        while len(left.items) > 0:
            item = left.items.pop()
            right.push(item)
        # pop "top" of right, save value to return later
        dequeued_item = right.pop()
        # pop all items in right back over to left
        while len(right.items) > 0:
            item = right.items.pop()
            left.push(item)
        return dequeued_item

    #ans holds popped items from the queue
    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())

    print('left-->', left.items)
    return ans

# test cases:
print(solution(["push 1", "push 2", "pop", "push 3", "pop"])) # [1, 2]
