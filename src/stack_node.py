# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 9/30/2022
# ----- Purpose ------
# This is a generic stack method that should not be affected by the data in which
# it is being used for
#
# ----- Description ------
# There are several simple functions, such as push, pop, init, size, is_empty,
# and peek to ensure that the stack operates as expected, and allows for future
#  functionality if needed


# this will set up a stack node
class StackNode:
    def __init__(self, data, top):
        self.data = data
        self.next = top


# this is to set up a stack class
class Stack:
    # initializes the stack
    def __init__(self):
        self.top = None
        self.height = 0

    # Appends the end of the stack
    def push(self, item):
        self.top = StackNode(item, self.top)
        self.height += 1

    # Pops the stack and returns the value popped to where it was called
    def pop(self):
        if not self.is_empty():
            temp = self.top.data
            self.top = self.top.next
            self.height -= 1
            return temp

    # Reads the value of the top stack
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return "Stack is empty"

    # Validates if the stack is empty or not
    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    # Due to planning for this in the class, this function reports
    # how many items are in the stack
    def size(self):
        return self.height

    # This function is to empty the stack, which the only use case for this
    # Specific function is to make sure to prevent memory leaks
    def empty_stack(self):
        while not self.is_empty():
            self.pop()
