from collections import deque

class Stack:
    def __init__(self):
        self.__stack = []

    def top(self):
        return self.__stack[-1]

    def pop(self):
        self.__stack.pop()

    def push(self, value):
        self.__stack.append(value)

    def empty(self):
        return not bool(self.__stack)

class Queue:
    def __init__(self):
        self.__queue = deque()

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        self.__queue.popleft()

    def top(self):
        return self.__queue[0]

    def empty(self):
        return not bool(self.__queue)

    def __iter__(self):
        return iter(self.__queue)

precedence = {
              "*" : 10,
              "/" : 10,
              "+" : 9,
              "-" : 9,
              "(" : -1,
              ")" : -1,
              }

operations = {
              "*" : lambda x, y: x * y,
              "/" : lambda x, y: x / y,
              "+" : lambda x, y: x + y,
              "-" : lambda x, y: x - y,
              }

expr = ["3", "-", "(", "2", "+", "30", ")"]

def infixTOprefix(expr, precedence):
    stack = Stack()
    output = Queue()

    for token in expr:
        if token not in precedence:
            output.enqueue(token)
        elif token == ")":
            while not stack.empty():
                if stack.top() == "(":
                    stack.pop()
                    break
                else:
                    output.enqueue(stack.top())
                    stack.pop()
        else:
            if stack.empty() or token == "(":
                stack.push(token)
            else:
                while not stack.empty() and precedence[token] <= precedence[stack.top()]:
                    output.enqueue(stack.top())
                    stack.pop()
                stack.push(token)

    while not stack.empty():
        output.enqueue(stack.top())
        stack.pop()
    return list(output)

def evaluate(expr, operations):
    stack = Stack()
    for token in expr:
        if token not in operations:
            stack.push(float(token))
        else:
            a = stack.top()
            stack.pop()
            b = stack.top()
            stack.pop()
            stack.push(operations[token](b, a))
    return stack.top()

prefix = infixTOprefix(expr, precedence)
print (expr)
print (prefix)
print (evaluate(prefix, operations))
