# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:54:46 2024

@author: Aditya
"""

#Given a integer k, find the sum of first k even-length palindrome numbers. 
#Even length here refers to the number of digits of a number is even.
#sum of 3 

def get_allPalindromeNum(k,num_Digits,n_Numbers):
    a=[10**(num_Digits-1),10**(k-1)]
    c=0
    #print(a)
    list_a=[]
    len_a = a[len(a)-1] - a[0]
    for x in range(0,len_a):
        b=str(a[0]+x)
        if b == str(b[::-1]) and (len(b))%2 != 0:
            list_a.append(b)
            print(list_a)
            if len(list_a) == n_Numbers:
                for x1 in range(0,n_Numbers):
                    c=c+int(list_a[x1])
                break
    return c
        
        
get_allPalindromeNum(4,3,5)

