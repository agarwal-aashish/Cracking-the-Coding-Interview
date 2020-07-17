'''
Cracking the Coding Interview
Problem Number 3.4
Problem Name: Queue via Stacks
Problem Description: Implement a MyQueue class which implements a queue using two stacks.
'''
class Stack:
    def __init__(self):
        self.stack=list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    
class MyQueue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    def enqueue(self,item):
        self.s1.push(item)
    def dequeue(self):
        if self.s1.size()==0 and self.s2.size()==0:
            return "Underflow"
        if self.s2.size()==0:
            while self.s1.size():
                self.s2.push(self.s1.pop())
        return self.s2.pop()
        
