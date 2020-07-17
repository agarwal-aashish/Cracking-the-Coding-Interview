'''
Cracking the Coding Interview
Problem Number 2.7
Problem Name: Intersection
Problem Description: Given two (singly) linked lists, determine if the two lists intersect. Return the inter- secting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.visited=False
def intersection(head1,head2):
    while head1!=None:
        head1.visited=True
        head1=head1.next
    while head2!=None:
        if head2.visited:
            return head2
        head2=head2.next
    return None
