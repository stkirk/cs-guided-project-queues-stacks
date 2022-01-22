# given a string called sequence consisting of opening and closing brackets []{}():
# determine whether or not the sequence has valid syntax

# init a stack to hold open brackets
# opening brackets add to stack, closing should peek at stack to see if they're the same type bracket and if they are pop the open bracket off the stack
# if they aren't the same type, syntax is invalid
# if the stack has anything in it when sequence is finished we have invalid syntax
# empty sequence is valid syntax

# stack class
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

def bracket_linter(sequence):
    # init bracket_stack
    bracket_stack = Stack()
    # loop through each bracket in sequence
    for bracket in sequence:
        # if its an open bracket
        if bracket == "(" or bracket == "[" or bracket == "{":
            # push onto bracket_stack
            bracket_stack.push(bracket)
        # it is a closed bracket:
        # if the stack is empty
        elif bracket_stack.isEmpty():
            return False
        # elif bracket is )
        elif bracket == ")":
            # if top of stack is (
            if bracket_stack.peek() == "(":
                    # pop it off stack
                    bracket_stack.pop()
            # else top of stack isn't (
            else:
                return False
        elif bracket == "]":
            # if top of stack is [
            if bracket_stack.peek() == "[":
                    # pop it off stack
                    bracket_stack.pop()
            # else top of stack isn't [
            else:
                return False
        # its a curly bracket:
        else:
            # if top of stack is {
            if bracket_stack.peek() == "{":
                    # pop it off stack
                    bracket_stack.pop()
            # else top of stack isn't {
            else:
                return False

    # loop finished, if stack is empty return true, if it isnt return False
    if bracket_stack.isEmpty():
        return True
    else:
        return False


print("true:", bracket_linter("()")) # True
print("true:", bracket_linter("()[]{}")) # True
print("false:", bracket_linter("(]")) # False
print("false:", bracket_linter("([)]")) # False
print("true:", bracket_linter("{[]}")) # True
