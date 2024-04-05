# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:13:59 2024

@author: Aditya
"""

#create palindrome / check if palindrome possible or not from string 
str1='a..xri..a'
str2=''
var1=0
def check_firstlastnchar(a):
    #print(a)
    loop_stat = 0
    list_a=list(a)
    len_a=len(list_a)
    for x in range(len_a):
        if list_a[x] == list_a[len_a-1-x]:  #if 0  == n-1 
            #print('1',list_a[x],list_a[len_a-1-x],x)  #cool
            if list_a[x]  == '.' and list_a[len_a-1-x] == '.':
               list_a[x]  = list_a[0] 
               list_a[len_a-1-x]  = list_a[0] #cool
        elif list_a[x] == '.' or list_a[len_a-1-x] == '.': 
            #print('2',list_a[x],list_a[len_a-1-x])  #if 0 = . and n = x then . becomes x 
            if list_a[x] == '.':
                list_a[x] = list_a[len_a-1-x]  #.becomes x
            else:
                list_a[len_a-1-x] = list_a[x] #vice versa 
                #print('3')
        else:
            print('Cannot be a palindrome as ',list_a[x],' <> ',list_a[len_a-1-x],'in position ',x+1,'in',a)
            loop_stat = 1
            break
    if loop_stat != 1:
        print('Palindrome is: ',str2.join(list_a))
    
check_firstlastnchar(str1)
