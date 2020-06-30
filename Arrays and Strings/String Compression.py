'''
Cracking the Coding Interview
Problem Number 1.6
Problem Name: String Compression
Problem Description: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''
s=input()
out=''
n=len(s)
i=0
while i<n:
    c=s[i]
    count=0
    while i<n and s[i]==c:
        i+=1
        count+=1
    out+=c+str(count)
if len(out)<n:
    print(out)
else:
    print(s)
    
