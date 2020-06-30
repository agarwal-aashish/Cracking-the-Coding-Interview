'''
Cracking the Coding Interview
Problem Number 1.5
Problem Name: One Away
Problem Description: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
'''
def oneedit(s1,s2,n):
    change=0
    for i in range(n):
        if s1[i]!=s2[i]:
            change+=1
        if change>1:
            return False
    return True

def onemodify(s1,s2,n,m):
    i=j=0
    flag=0
    while i<n and j<m:
        if s1[i]!=s2[j]:
            if flag:
                return False
            flag=1
            if n<m:
                i-=1
            else:
                j-=1
        i+=1
        j+=1

s1=input()
s2=input()
n=len(s1)
m=len(s2)
if n==m:
    print(oneedit(s1,s2,n))
elif abs(n-m)==1:
    print(onemodify(s1,s2,n,m)
else:
    print(False)
