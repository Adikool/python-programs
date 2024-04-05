# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 22:09:49 2024

@author: Aditya
"""

#Longest Non Palindromic Substring

a='googoog'
def is_nonpalindrome(a):
    if a == a[::-1]:
        return 0
    else:
        return len(a)

#print(is_nonpalindrome(a))

var2=1
c=0
c1=''
for var1 in range(len(a)+1):
    for x in range(len(a)+1):
        #print(x,var1,a[var1:x])
        if c < is_nonpalindrome(a[var1:x]):
            c=is_nonpalindrome(a[var1:x])
            c1=a[var1:x]
        else:
            pass

print(c,c1)
