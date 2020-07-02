'''
Cracking the Coding Interview
Problem Number 2.2
Problem Name: Return Kth to Last
Problem Description: Implement an algorithm to find the kth to last element of a singly linked list.
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
n,k=map(int,input().split())
if k>n:
    print("Out of bounds")
else:
    head=last=None
    for i in range(n):
        t=node(int(input()))
        if head==None:
            head=t
        else:
            last.next=t
            t.prev=last
        last=t
    t=head
    c=1
    while c<k:
        c+=1
        t=t.next
    else:
        t1=head
        while t.next!=None:
            t=t.next
            t1=t1.next
        print(t1.data)
