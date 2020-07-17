'''
Cracking the Coding Interview
Problem Number 3.3
Problem Name: Stack of Plates
Problem Description: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack (that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index)which performs apopoperation on a specific sub-stack.
'''
class SetofStacks:
    def __init__(self,threshold):
        self.threshold=threshold
        self.stack=[]
        self.cur=-1
    def push(self,item):
        if self.cur==-1:
            self.stack.append([item])
            self.cur=0
        elif len(self.stack[self.cur])<self.threshold:
            self.stack[self.cur].append(item)
        else:
            self.cur+=1
            self.stack.append([item])
    def pop(self):
        if self.cur==-1:
            return "Underflow"
        x=self.stack[self.cur].pop()
        if len(self.stack[self.cur])==0:
            self.stack.pop()
            self.cur-=1
        return x
    def popAt(self,index):
        if self.cur>=index:
            x=self.stack[index].pop()
            if len(self.stack[index])==0:
                self.stack.pop(index)
                self.cur-=1
            return x
        return "Index greater than available stacks"
        
