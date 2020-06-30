'''
Cracking the Coding Interview
Problem Number 1.1
Problem Name: Is Unique
Problem Description: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''

s=input()
#solution with extra space but O(n) complexity
used=set()
for i in s:
    if i in used:
        print(False)
        break
    used.add(i)
else:
    print(True)

'''
solution with no extra space but O(n log n) complexity
def fun(s):
    n=len(s)
    if n>26:
        return False
    s.sort()
    for i in range(n-1):
        if s[i]==s[i+1]:
            return False
    return True

fun(list(s))
'''
