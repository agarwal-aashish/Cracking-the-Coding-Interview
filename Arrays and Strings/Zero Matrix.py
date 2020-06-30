'''
Cracking the Coding Interview
Problem Number 1.8
Problem Name: Zero Matrix
Problem Description: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
'''
m,n=map(int,input().split())
mat=[]
zero=[]
for i in range(m):
    l=list(map(int,input().split()))
    mat.append(l.copy())
for i in range(m):
    for j in range(n):
        if mat[i][j]==0:
            zero.append([i,j])
for k in zero:
    r,c=k[0],k[1]
    for i in range(n):
        mat[r][i]=0
    for i in range(m):
        mat[i][c]=0
for i in mat:
    for j in i:
        print(j,end=' ')
    print()
