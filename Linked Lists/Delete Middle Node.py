'''
Cracking the Coding Interview
Problem Number 2.3
Problem Name: Delete Middle Node
Problem Description: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
'''
def delnode(node):
    t=node.next
    node.data=t.data
    node.next=t.next
    del(t)

        
