#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
 Try the same thing, but have the program choose a random word from the dictionary,
and then ask the user to guess the word. (You might want to limit yourself to words containing between 2-5 letters,
to avoid making it too horribly difficult.) Instead of telling the user that they should guess a smaller or larger number,
have them choose an earlier or later word in the dictionary.
'''

import random

dict1 = {'hello': 5, 'I': 1, 'am': 2, 'hell': 3, 'ugly': 4}

print('The dictionary is:')
for key, value in dict1.items():
    print(key, ':', value)

counter = 0

b = random.randint(1, 4)

while counter != 3:
    str1 = input('please choose a random word from the dictionary\n')
    print(type(str1))
    if dict1[str1]< b:
        print('too low')
        counter +=1
    elif dict1[str1]>b:
        print('too high')
        counter +=1
    else:
        print('just right')
