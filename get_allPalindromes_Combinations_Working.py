# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:02:06 2024

@author: Aditya
"""

import itertools
import math

def get_allPalindromes(str1):
    list_final=[]
    mid_len=math.floor(len(str1)/2)
    for v in itertools.permutations(list(str1)):
        if ''.join(v)[0:mid_len] == ''.join(v)[::-1][0:mid_len] :
            list_final.append(''.join(v))
    print('All palindromes')
    print(set(list_final))

get_allPalindromes('aabbccd')

#get all combinations irresp of length 

def get_all_len_Palindromes(str1):
    list_final=[]
    for x in range(2,len(str1)+1):
        mid_len=math.floor(x/2)    
        for v in itertools.permutations(list(str1),x):
            if ''.join(v)[0:mid_len] == ''.join(v)[::-1][0:mid_len] :
                list_final.append(''.join(v))
    print(set(list_final))

get_all_len_Palindromes('aaaabcccc')

def get_catalanCombinations(str1):
    list_final=[]
    for v in itertools.permutations(list(str1)):
        #first should not be closing , last should not be opening and combination should not be existing
        if ''.join(v)[0:1] != ')' and ''.join(v)[::-1][0:1] != '(' and ''.join(v) not in list_final:
            list_final.append(''.join(v))
    
    list_final2 = list_final.copy()
    for cntr2 in range(len(list_final)):
        strx=list_final[cntr2]
        tmp_list2=[]
        tmp_list1=[]
        #all opening in one list ; all closing in other list
        #positions of opening should be less than closing
        for i in range(len(strx)):
            if strx[i] == '(':
                tmp_list1.append(i)
            else:
                tmp_list2.append(i)
        for i1 in range(len(tmp_list1)):
            if tmp_list1[i1] > tmp_list2[i1]: #this cleans up junk!
                list_final2.remove(strx)
                break
    print(set(list_final2))

get_catalanCombinations('(())()') 

#def run_complex_operations(operation, input, pool):
#    pool.map(operation, input)

#processes_count = 10

#if __name__ == '__main__':
#    processes_pool = Pool(processes_count)
#    run_complex_operations(get_all_len_Palindromes('aaabcccdddff'), range(10), processes_pool)   


#get_catalanCombinations('()))((()') 

#logic is that after all combinations, list with ( should have lesser index elements wrt each position in temp_list2
#"(())" and "()()" 
#{')(()', '())('}  
#aaaabccccff
#get_all_len_Palindromes('aaaabcccc')    

#aaabcccdddl

