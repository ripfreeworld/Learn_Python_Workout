# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:29:54 2019

@author: changyu
"""

import random

def InputCheck(str):
    while str.isdigit()==False:
        print('input is not a number')
        str= input('give me a number in dictionary')
        str.isdigit
    else:
        return int(str)
    
dict = {'i':0, 'am':1, 'your':2,'father':3}
print('dictionary:')
for key, value in dict.items():
    print(key,':',value)
    
a=random.randint(0,len(dict)-1)

print('please give me the number of your choise')
b= input('guess a word in Dictionary: ')
b = InputCheck(b)

dictList= []
for key in dict.keys():
    dictList.append(key)


counter = 0 
while counter != 2:
    
        
    while a != dict[dictList[b]]:
        
        
        if a > dict[dictList[b]]:
            print('later word')
            b = input('input again:')
            b = InputCheck(b)
            counter+=1
            break
        else:
            print('earlier word')
            b = input('input again:')
            b = InputCheck(b)
            counter+=1
            break
        
    else:
        print(dictList[a],'is the right word!')
        break
        
else:
    print('you didnt guess in time')