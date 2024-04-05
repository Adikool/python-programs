# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:48:36 2024

@author: Aditya
"""

str1='aabcb'
#loop and get count 
import regex as re
final_result=[]
def getString2(str1,repl_char,cnt):
    str2=list(str1)
    str2=list(set(str2))
    if cnt !=1 :
        return str1.replace(str(repl_char), '', cnt-1)
    else:
        return str1

    
def getString(str1):
    str2=list(str1)
    str2=list(set(str2))
    #print(str2)
    result = ''
    for x in range(len(str2)):
        cnt=len(re.findall(str2[x],str1))
        if x == 0:
            result=getString2(str1,str2[x],cnt)
        else:
            result=getString2(result,str2[x],cnt)

    return result

print(getString(str1))

