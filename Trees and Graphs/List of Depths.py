'''
Cracking the Coding Interview
Problem Number 4.3
Problem Name: List of Depths
Problem Description: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
'''
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def insert(self,data):
        t=ListNode(data)
        if not self.head:
            self.head=t
        else:
            self.last.next=t
        self.last=t
    def printList(self):
        if not self.head:
            return
        print(self.head.data,end='')
        t=self.head.next
        while t!=None:
            print("-->",t.data,end='')
            t=t.next
            

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.depth=0

class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if self.root==None:
            t=Node(data)
            self.root=t
            print("Inserted")
            return
        print("Enter L or R of :",root.data)
        ch=input()
        if ch=='L':
            if root.left==None:
                t=Node(data)
                root.left=t
                print("Inserted")
            else:
                return self.insert(root.left,data)
        else:
            if root.right==None:
                t=Node(data)
                root.right=t
                print("Inserted")
            else:
                return self.insert(root.right,data)

def generateLists():
    global l,t
    if t.root==None:
        return
    queue=[t.root]
    t.root.depth=0
    while len(queue):
        cur=queue.pop(0)
        if len(l)<=cur.depth:
            li=LinkedList()
            l.append(li)
        li.insert(cur.data)
        if cur.left:
            queue.append(cur.left)
            cur.left.depth=cur.depth+1
        if cur.right:
            queue.append(cur.right)
            cur.right.depth=cur.depth+1

t=BinaryTree()
n=int(input("Enter number of nodes"))
for i in range(n):
    t.insert(t.root,int(input()))
l=[]
generateLists()
for i in range(len(l)):
    print("Depth",i,end=': ')
    l[i].printList()
    print()
