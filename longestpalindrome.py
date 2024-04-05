# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 18:35:32 2024

@author: Aditya
"""

#a='xyz'
#a='Too hot toh oot'
a='Madam Arora teaches aaMalayalamaa'
#a='tskeegofrfogeekst'
#a='laalirilaalcivic'
#a='cliriirilc'
#a='bbbaaaaalaaaaabbb'
#print(a[::-1])
''
a=a.replace(' ', '')
a=a.lower()
def is_palindrome(a):
    if a == a[::-1]:
        return len(a)
    else:
        #print('Not a Palindrome')
        return 0

#logic pass len of string ; 0 to len of string find all combinations of substrings; 01,11,12 etc

x=len(a)
print(x)
#var1=7
maxval=0
maxsubstr=''
for var1 in range(x+1): #0-9 #1
    for i in range(x+1): #0-9 #1-9
        is_pal = is_palindrome(a[i:i+var1]) #a[1:9] ; 0:1,0:2, 1:2;1:3..1:9
        if is_palindrome(a[i:i+var1]) > 1:
            if maxval <  is_pal:
                maxval = is_pal
                maxsubstr=a[i:i+var1]
print(maxval,maxsubstr)

#laalirilacivic
#la
