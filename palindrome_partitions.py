# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:49:53 2024

@author: Aditya
"""

def get_Palindrom_Partitioning(a):
    x=len(a)
    final_val=''
    max_final_val=''
    max_val=0
    part_res=[]
    for var1 in range(x+1): #0 1 2
        for i in range(x+1): #subset 0+1 1+1 1+2... 
            if a[i:i+var1] == a[i:i+var1][::-1] and len(a[i:i+var1])>1 :
                final_val=a[i:i+var1]
                if max_val < len(final_val):
                   max_val = len(final_val)    
                   max_final_val=final_val
    d=list(a)
    print(final_val) #get max length palindrome and exclude whatever is not required 
    for var2 in range(len(d)):  
        if d[var2] not in set(list(final_val)):
            part_res.append(d[var2])
    if len(max_final_val)==0:
        print(len(a)-1,'cut required, longest palindrome is',max_final_val,'partitions are',part_res)
    else:
        print(len(a)-len(max_final_val),'cut required, longest palindrome is',max_final_val,'partitions are',part_res)    

        
get_Palindrom_Partitioning('aaaacb')


