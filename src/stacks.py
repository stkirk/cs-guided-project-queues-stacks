# Stacks: last-in first-out, LIFO
# Think of a stack of plates
# Operations on a stack:
    # POP: remove item from top of the stack
    # PUSH: add item to top of the stack
# Bonus operations:
    # PEEK: look at item at top of stack but don't do anything to it
    # IS_EMPTY: returns True if no items in stack, else false if items in stack

# stock ListNode:
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<ListNode({self.value})>"

# Stack example:
class Stack:
    def __init__(self):
        # just need to keep track of head so new nodes can be put in front of it "on top of the stack"
        self.head = None

    # override the __str__ method, which is used to print
    # print something like this: (1)->(2)->(3)
    def __str__(self) -> str:
        lst_str = []
        current_node = self.head
        while current_node is not None:
            lst_str.append(f"({current_node.value})")
            current_node = current_node.next

        return "->".join(lst_str)

    # push new node onto front/top of stack   
    def push(self, new_node):
        # link new_node to existing head to put it at top of stack
        new_node.next = self.head
        # re-assign head to new_node
        self.head = new_node

    # pop node(head) off of front/top of stack
    def pop(self):
        # guard against popping an empty stack
        if self.head is None:
            return None
        # store current head
        old_head = self.head
        # reset head to next node in the stack (underneath old_head)
        self.head = self.head.next
        # overwrite old_head's next pointer
        old_head.next = None
        # send back the popped node, old_head
        return old_head
    
    # return head node without changing anything
    def peek(self):
        return self.head

    # return True/False depending on if the stack is empty or not
    def is_empty(self):
        return self.head is None

example_stack = Stack()
example_stack.push(ListNode(1))
example_stack.push(ListNode(2))
example_stack.push(ListNode(3))

print('example_stack', example_stack)

print("first pop-->", example_stack.pop()) #3
print("second pop-->", example_stack.pop()) #2
print('example stack after pop-->', example_stack)
print("second pop-->", example_stack.pop()) #1
print("second pop-->", example_stack.pop()) #None

example_stack.push(ListNode(4))
example_stack.push(ListNode(5))
print('example stack after pop and push-->', example_stack)
print('peek method', example_stack.peek())

print("pop-->", example_stack.pop()) #5
print("pop-->", example_stack.pop()) #4
print("is_empty method", example_stack.is_empty())
