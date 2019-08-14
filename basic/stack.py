# stack is list of elements organized by LIFO principle
class Stack:

    # create new stack
    def __init__(self):
        self.items = []

    # validate stack is empty
    def isEmpty(self):
        return self.items == []

    # add to stack new item
    def push(self, item):
        self.items.append(item)

    # return and remove last item
    def pop(self):
        return self.items.pop()

    # return last item
    def peek(self):
        return self.items[len(self.items)-1]

    # return stack size
    def size(self):
        return len(self.items)


# Simple parentheses checker
def parentheses_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parentheses_checker('((((((())'))
print(parentheses_checker('(((())))'))
print(parentheses_checker('(()'))


# General parentheses checker
def parentheses_checker_2(symbol_string):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = '({['
    closers = ')}]'
    if opens.index(open) == closers.index(close):
        return True
    else:
        return False


print(parentheses_checker_2('{({([][])}())}'))
print(parentheses_checker_2('[{()]'))


# Algorithm for convert decimal number to binary
def divide_by_2(number):
    s = Stack()
    while 0 < number:
        rem = number % 2
        s.push(rem)
        number = number // 2

    bin = ''
    while not s.isEmpty():
        bin = bin + str(s.pop())

    return bin


print(divide_by_2(100))


# From decimal to ant base converter
def base_converter(number, base):
    s = Stack()
    digits = '0123456789ABCDEF'

    while 0 < number:
        rem = number % base
        s.push(rem)
        number = number // base

    string = ''
    while not s.isEmpty():
        string = string + digits[s.pop()]

    return string


print(base_converter(25, 2))
print(base_converter(25, 16))