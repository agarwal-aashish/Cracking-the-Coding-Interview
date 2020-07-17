'''
Cracking the Coding Interview
Problem Number 2.8
Problem Name: Loop Detection
Problem Description: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINI TION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A -) B -) C -) 0 -) E -) C [the same C as earlier]
Output: C
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        self.visit=False
def loop(head):
    t=head
    while t.visit==False:
        t.visit=True
        t=t.next
    if t==head:
        return True
    return False
