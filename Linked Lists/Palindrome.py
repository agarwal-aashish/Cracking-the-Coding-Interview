'''
Cracking the Coding Interview
Problem Number 2.6
Problem Name: Palindrome
Problem Description: Implement a function to check if a linked list is a palindrome.
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def isPalindrome(head,last):
    while head!=last:
        if head.data!=last.data:
            return False
        head=head.next
        if head==last:
            return True
        last=last.prev
    return True
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
print(isPalindrome(head,last))
