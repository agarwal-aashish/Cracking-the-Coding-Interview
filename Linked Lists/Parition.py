'''
Cracking the Coding Interview
Problem Number 2.4
Problem Name: Partition
Problem Description: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need to be after the elements less than x (see below).The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def fun(head,pivot):
    new=tail=None
    while head!=None:
        t=node(head.data)
        if new==None:
            new=tail=t
        elif t.data<pivot:
            t.next=new
            new=t
        else:
            tail.next=t
            tail=t
        head=head.next
    return new
            
    

n,pivot=map(int,input().split())
head=last=None
for i in range(n):
    t=node(int(input()))
    if head==None:
        head=t
    else:
        last.next=t
        t.prev=last
    last=t
head=fun(head,pivot)
i=head
while i!=None:
    print(i.data,end=' ')
    i=i.next
