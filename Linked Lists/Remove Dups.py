'''
Cracking the Coding Interview
Problem Number 2.1
Problem Name: Remove Dups
Problem Description: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def fun(head):
    freq=set()
    t=head
    while t!=None:
        if t.data in freq:
            x=t
            t.prev.next=t.next
            if t.next:
                t.next.prev=t.prev
            t=t.next
            del(x)
        else:
            freq.add(t.data)
            t=t.next
    return head

def fun1(head):
    t=head
    while t!=None:
        t1=t.next
        while t1!=None:
            if t1.data==t.data:
                x=t1
                t1.prev.next=t1.next
                if t1.next:
                    t1.next.prev=t1.prev
                t1=t1.next
                del(x)
            else:
                t1=t1.next
        t=t.next
    return head

n=int(input())
head=last=None
for i in range(n):
    t=node(int(input()))
    if head==None:
        head=t
    else:
        last.next=t
        t.prev=last
    last=t


head=fun(head) #solution in O(n) time but with extra space
#head=fun1(head) #solution in O(n^2) time but no extra space
i=head
while i!=None:
    print(i.data,end=' ')
    i=i.next
