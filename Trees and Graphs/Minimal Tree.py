'''
Cracking the Coding Interview
Problem Number 4.2
Problem Name: Minimal Tree
Problem Description: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
'''
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if self.root==None:
            t=Node(data)
            self.root=t
            return
        if data<root.data:
            if root.left==None:
                t=Node(data)
                root.left=t
            else:
                self.insert(root.left,data)
        else:
            if root.right==None:
                t=Node(data)
                root.right=t
            else:
                self.insert(root.right,data)
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data,end=' ')
        self.inorder(root.right)
    def preorder(self,root):
        if root==None:
            return
        print(root.data,end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=' ')

def generateTree(l,lo,hi):
    global t
    if lo>hi:
        return
    mid=(lo+hi)//2
    t.insert(t.root,l[mid])
    generateTree(l,lo,mid-1)
    generateTree(l,mid+1,hi)

n=int(input("Enter size of array"))
l=list(map(int,input().split()))
t=BST()
generateTree(l,0,n-1)
