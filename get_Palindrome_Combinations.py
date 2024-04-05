# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:49:15 2024

@author: Aditya
"""

#Input:  str = "aabcb"
#Output: abcba bacab

#abcba 
#bacab

#get all combinations of palindrome
#get char and their counts
#0 and n-1 logic

import regex as re
import itertools
def get_Palindrome_Combinations(str1):
    final_str=''
    list_tmp=[]
    list_final=[]
    mid_char=''
    list_2 = list(set(list(str1)))
    list_2.sort()
    for x in range(0,len(list_2)):
        count= len(re.findall(list_2[x], str1))
        #print(count)
        if count%2 == 1:
            list_tmp.append(list_2[x])
            mid_char=list_2[x]
        else:
            final_str=str(final_str)+str(list_2[x])
    
    #below will go into one input, need to have iteration for other combinations
    for v in itertools.permutations(list(final_str)):
        list_final.append(''.join(v))
    #print(list_final)
    for x4 in range(len(list_final)):
        a=list_final[x4]+mid_char+list_final[x4][::-1]
        #print(a)
    
    list_final1=[]
    print(str1)
    print(str1[0:3])
    for v1 in itertools.permutations(list(str1)):
        init_char=''.join(v1[0:3])
        list_final1.append(init_char+mid_char+init_char[::-1])
    print(list_final1)
        

get_Palindrome_Combinations('aabbccd')
#aaaabccccbbbd
#abcdcba
#cbadabc
#bcadacb
#cabdbac
#bacdcab
