# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:35:15 2024

@author: Aditya
"""

#For example if the given range is {10, 115}
#then output should be {11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111}

def get_allPalindromeNum(a):
    list_a=[]
    len_a = a[len(a)-1] - a[0]
    for x in range(0,len_a):
        b=str(a[0]+x)
        if b == str(b[::-1]):
            list_a.append(b)
    print(list_a)
        
        

a=[10,115]
get_allPalindromeNum([10,1150])