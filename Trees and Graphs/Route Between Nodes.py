'''
Cracking the Coding Interview
Problem Number 4.1
Problem Name: Route Between Nodes
Problem Description: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''
class Graph:
    def __init__(self,vertices):
        self.l=[dict() for i in range(vertices)]
        self.v=vertices
    def addEdge(self,v1,v2,weight=1):
        if v1<0 or v2<0 or v1>=self.v or v2>=self.v:
            return "Out of bounds"
        self.l[v1][v2]=weight
    def removeEdge(self,v1,v2):
        if v1<0 or v2<0 or v1>=self.v or v2>=self.v:
            return "Out of bounds"
        if v2 in self.l[v1]:
            self.l[v1].pop(v2)
    def adj(self,vertex):
        l=[]
        for i in self.l[vertex]:
            l.append(i)
        return l
    def bfs(self,source,destination):
        if source>=self.v or source<0:
            return "Out of boounds"
        if source==destination:
            return "Same nodes"
        queue=[]
        visited=set()
        visited.add(source)
        queue.append(source)
        while len(queue):
            cur=queue.pop(0)
            print(cur,end=' ')
            l=self.adj(cur)
            for i in l:
                if i==destination:
                    return "Path exists"
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return "No path exists"
    
n=int(input("Enter number of vertices: "))
G=Graph(n)
e=int(input("Enter number of edges to insert"))
for i in range(e):
    v1,v2=map(int,input().split())
    G.addEdge(v1,v2)
print("Enter source and destination")
s,d=map(int,input().split())
G.bfs(s,d)
