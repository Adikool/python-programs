# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 19:16:07 2024

@author: Aditya
"""
import regex as re
#a='aabbc'
#a='geeksforgeeks' #tskeegforfogeekst geeksforgeekst
a='baaabxxx'
print(len('geeksforgeeks'),len('skeegofrfogeeks'))
#a='lirilciric'
#a='cliriirilc'
#print(a[::-1])
#check no of repititons of letters
#only one character can be repeated
b=list(a)
b.sort()
print(b)
c=0
b= list(set(a))
print(b)
for i in range(len(b)):
    count = len(re.findall(b[i], a)) #find count of each letter, only one leter can only have odd occurrences 
    #print(count)
    c+=(count%2)  #count should be divisible by 2 ; #sum all divisible by 2 cs 
    print(c,count,count%2,b[i])  
    
#print(c%2)
if (c == 0):
    print('Can be a palindrome',c)
elif (c%2 == 0 & c != 0) | c != 1:  #if c%2 = 0 means there are two odds , if c=0 no odds, if c= 1 then only one odd and c should not be 0 because 0 % 0 is 0 
    print("Cannot be a palindrome",c-1)
else:
    print("Can be a palindrome",c)
