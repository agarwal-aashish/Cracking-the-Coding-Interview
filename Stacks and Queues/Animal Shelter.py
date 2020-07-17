'''
Cracking the Coding Interview
Problem Number 3.6
Problem Name: Animal Shelter
Problem Description: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked List data structure.
'''
class node:
    def __init__(self,IDNo,typeOfAnimal):
        self.id=IDNo
        self.typeOfAnimal=typeOfAnimal
        self.next=None
        self.prev=None

class AnimalShelter:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,IDNo,typeOfAnimal):
        t=node(IDNo,typeOfAnimal)
        if self.head==None:
            self.head=t
        else:
            self.last.next=t
            t.prev=self.last
        self.last=t
    def dequeueAny(self):
        if self.head==None:
            return "No animals in the shelter"
        print(self.head.id,self.head.typeOfAnimal)
        x=self.head
        if self.head==self.last:
            self.head=self.last=None
        else:
            self.head=self.head.next
            self.head.prev=None
        del(x)
    def dequeueDog(self):
        t=self.head
        while t!=None and t.typeOfAnimal!='Dog':
            t=t.next
        if t==None:
            return "No dogs in shelter"
        print(t.id)
        if t==self.last:
            self.last=self.last.prev
            self.last.next=None
        elif t==self.head:
            self.head=self.head.next
            self.head.prev=None
        else:
            t.next.prev=t.prev
            t.prev.next=t.next
        del(t)
    def dequeueCat(self):
        t=self.head
        while t!=None and t.typeOfAnimal!='Cat':
            t=t.next
        if t==None:
            return "No cats in shelter"
        print(t.id)
        if t==self.last:
            self.last=self.last.prev
            self.last.next=None
        elif t==self.head:
            self.head=self.head.next
            self.head.prev=None
        else:
            t.next.prev=t.prev
            t.prev.next=t.next
        del(t)
