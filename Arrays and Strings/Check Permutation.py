'''
Cracking the Coding Interview
Problem Number 1.2
Problem Name: Check Permutation
Problem Description: Given two strings, write a method to decide if one is a permutation of the
other.
'''
def method(str1,str2):
    freq1=dict()
    freq2=dict()
    for i in str1:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i]=1
    for i in str2:
        if i in freq2:
            freq2[i]+=1
        else:
            freq2[i]=1
    for i in freq1.keys():
        if i not in freq2 or freq1[i]!=freq2[i]:
            return False
    return True
