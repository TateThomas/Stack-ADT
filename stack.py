'''
Stack ADT
CS 2420
Author: Tate Thomas

Stack class:

    Methods:
    push(item): push an item onto the stack. Size increases by 1.
    pop(): remove the top item from the stack and return it. Raise an
        IndexError if the stack is empty.
    top(): return the item on top of the stack without removing it.
        Raise an IndexError if the stack is empty.
    size(): return the number of items on the stack.
    clear(): empty the stack.
'''

class Stack:
    '''Stack class:

    Methods:
    push(item):
    pop():
    top():
    size():
    clear():
    '''

    def __init__(self):
        '''Initializes empty container for stack'''

        self._stack = []

    def push(self, item):
        '''Pushes item onto the top of stack'''

        self._stack.append(item)

    def pop(self):
        '''Pops item off of the top of stack'''

        if len(self._stack) == 0:
            raise IndexError("Stack is currently empty; can not pop.")
        item = self._stack.pop(-1)
        return item

    def top(self):
        '''Returns what's on the top of the stack.'''

        if len(self._stack) == 0:
            raise IndexError("Stack is currently empty; no items on top.")
        return self._stack[-1]

    def size(self):
        '''Return the size of the stack'''

        return len(self._stack)

    def clear(self):
        '''Clears the stack'''

        self._stack = []

    def __str__(self):
        '''Returns the stack as a string'''

        return str(self._stack)
