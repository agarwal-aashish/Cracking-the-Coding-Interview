'''
Cracking the Coding Interview
Problem Number 2.5
Problem Name: Sum Lists
Problem Description: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-) 1 -) 6) + (5 -) 9 -) 2).Thatis,617 + 295. Output: 2 -) 1 -) 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295. Output: 9 -) 1 -) 2.That is, 912.
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def createlist(num):
    head=None
    for i in num:
        t=node(int(i))
        if head==None:
            head=t
        else:
            tail.next=t
        tail=t
    return head

def fun(h1,h2):
    num1=num2=''
    while h1!=None:
        num1=int(str(h1.data)+str(num1))
        num2=int(str(h2.data)+str(num2))
        h1=h1.next
        h2=h2.next
    num=num1+num2
    num=str(num)
    return createlist(num[-1::-1])

def followup(h1,h2):
    num1=num2=0
    while h1!=None:
        num1=(num1*10)+h1.data
        num2=(num2*10)+h2.data
        h1=h1.next
        h2=h2.next
    num=num1+num2
    num=str(num)
    return createlist(num)

n=int(input())
head=last=None
print("Enter linked list 1")
for i in range(n):
    t=node(int(input()))
    if head==None:
        head=t
    else:
        last.next=t
        t.prev=last
    last=t
h1=head
head=last=None
print("Enter linked list 2")
for i in range(n):
    t=node(int(input()))
    if head==None:
        head=t
    else:
        last.next=t
        t.prev=last
    last=t
h2=head
list1=fun(h1,h2)
list2=followup(h1,h2)
i=list1
while i!=None:
    print(i.data,end=' ')
    i=i.next
i=list2
print()
while i!=None:
    print(i.data,end=' ')
    i=i.next
