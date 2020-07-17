'''
Cracking the Coding Interview
Problem Number 3.5
Problem Name: Sort Stack
Problem Description: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
'''
class SortStack:
    def __init__(self):
        self.stack=list()
        self.temp=list()
    def isEmpty(self):
        if len(self.stack):
            return False
        return True
    def stacksort(self):
        while not self.isEmpty():
            x=self.stack.pop()
            while len(self.temp) and self.temp[-1]>x:
                self.stack.append(self.temp.pop())
            self.temp.append(x)
        while len(self.temp):
            self.stack.append(self.temp.pop())
    def push(self,item):
        self.stack.append(item)
        self.stacksort()
    def pop(self):
        if self.isEmpty():
            return "Underflow"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Underflow"
        return self.stack[-1]
