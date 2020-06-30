'''
Cracking the Coding Interview
Problem Number 1.9
Problem Name: String Rotation
Problem Description: Assume you have amethod isSubstring which checks ifone word is asubstring of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one call to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").
'''
def isSubstring(s1,s2):
    n=len(s1)
    i=0
    m=len(s2)
    while i<n-m+1:
        j=0
        while j<m:
            if s2[j]!=s1[i]:
                break
            i+=1
            j+=1
        else:
            return True
        i+=1
    return False
            
        

s1=input()
s2=input()
print(isSubstring(s1+s1,s2))
