
from src.stack_node import Stack

# to postfix expression
def evaluatePostfix(postfix):
    stack = Stack()
    # Iterate over the expression for conversion
    for i in postfix:
        if i.isdigit():
            stack.push(i)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if i == "%" or i == "/":
                if val1 == 0 or val2 == 0:
                    return "Invalid, cannot divide, or divide by, 0"
            elif i is None or val1 is None or val2 is None:
                return "Invalid expression, none value included ha"
            else:
                combo = 0
                if i == "+":
                    combo = int(val2) + int(val1)
                elif i == "-":
                    combo = int(val2) - int(val1)
                elif i == "*":
                    combo = int(val2) * int(val1)
                elif i == "/":
                    combo = int(val2) / int(val1)
                elif i == "$":
                    combo = int(val2) ^ int(val1)
                stack.push(combo)
    value = stack.pop()
    if value is None:
        return "Invalid expression, none value included"
    else:
        return value
