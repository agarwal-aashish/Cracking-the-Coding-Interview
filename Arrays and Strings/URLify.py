'''
Cracking the Coding Interview
Problem Number 1.3
Problem Name: URLify
Problem Description: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string
'''
def method(string):
    new=''
    for i in string:
        if i!=' ':
            new+=i
        else:
            new+='%20'
    return new
