# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:50:46 2019

@author: changyu
"""

import random

def InputCheck(str):
    while str.isdigit()==False:
        print('input is not a number')
        str= input('input a value between 1 and 100:')
        str.isdigit
    else:
        return int(str)


a=random.randint(0,100)
b= input('input a value between 1 and 100:')
b= InputCheck(b)

while a != b:
    if a > b:
        print('too low')
        b = input('input again:')
        b = InputCheck(b)
    else:
        print('too high')
        b = input('input again:')
        b = InputCheck(b)
    
else:
    print('right number!')
        
