'''
Cracking the Coding Interview
Problem Number 1.4
Problem Name: Palindrome Permutation:
Problem Description: Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
'''
s=input()
freq=dict()
for i in s:
    if i==' ':
        continue
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
odd=False
for i in freq.keys():
    c=freq[i]
    if c%2==0:
        continue
    else:
        if odd:
            print(False)
            break
        odd=True
else:
    print(True)
