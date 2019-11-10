# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:38:59 2019

@author: changyu
"""

def PigLatin(a):
    
    if a[0] in ('a','e','i','o','u'):
        a+='way'
        return print(a)
    else:
        a=a+a[0]+'ay'
        a=a.replace(a[0],'')
        return print(a)
    
a=input('please enter your word: ') 
PigLatin(a)

    
    
    

    
    