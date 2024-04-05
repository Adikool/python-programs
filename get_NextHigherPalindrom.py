# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:24:27 2024

@author: Aditya
"""

#find next higher palindrome number after - 4697557964
import math 
import itertools 
def get_nextHigherPalindrome(str2):
    list_final=[]
    str1=str(str2)
    mid_len=math.floor(len(str1)/2)
    for v in itertools.permutations(list(str1)):
        perm_str=''.join(v)
        #print(perm_str,perm_str[0:mid_len] , perm_str[::-1][0:mid_len] ,int(perm_str) , str2,list_final)
        if perm_str[0:mid_len] == perm_str[::-1][0:mid_len] and int(perm_str) > str2 and int(perm_str) not in list_final and len(list_final) < 1:
            list_final.append(int(perm_str))
    if len(list_final) > 0:
        print(list_final[0])
    else:
        print("Not possible")
    
    
    
get_nextHigherPalindrome(1221)
#2121
#4697557964
