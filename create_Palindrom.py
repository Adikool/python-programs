# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:19:40 2024

@author: Aditya
"""

import regex as re
import math as m
#Input:  str = "aaaad" ; Output: aadaa
def create_Palindrom(str1):
    a=list(str1)
    b=list(set(a))
    c=[]
    a.sort()
    for x in range(len(b)):
        u=len(re.findall(b[x],str1))
        if u == 1:
            c.append(u)
    if len(c) == 1:        
        pos_str1= m.floor(len(str1)/2)
        repl_Str = str1.replace(b[x], str1[pos_str1])
        print (repl_Str[:pos_str1] + b[x] + repl_Str[pos_str1+1:])

#create_Palindrom('aaaad')
create_Palindrom('aaaapbbbb')
#keep middle element fixed, first second element can be alternating 


