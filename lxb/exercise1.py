#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Write a program that chooses a random integer between 0 and 100(inclusive)
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of:
Too high; Too low; Just right
If the user guessed correctly, then the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.
Note:
If the user simply presses Enter when presented with the input prompt,
the value returned by input is an empty string, not None. Indeed, the return value from input will always be a string,
regardless of what the user entered.
2019/11/03 更新：
### Update the Exercise 1:
1. Modify this program, such that it gives the user only 3 chances to guess the correct number.
If they try three times without success, they’re told that they didn’t guess in time, and the program exits.

2. Not only should you choose a random number, but you should also choose a random number base, from 2 to 16,
in which the user should submit their input. If the user inputs "10" as their guess,
you’ll need to interpret it in the correct number base; "10" might mean 10 (decimal) or 2 (binary) or 16 (hexadecimal).~~ (个人觉得比较麻烦，用处不大)

3. Try the same thing, but have the program choose a random word from the dictionary,
and then ask the user to guess the word. (You might want to limit yourself to words containing between 2-5 letters,
to avoid making it too horribly difficult.) Instead of telling the user that they should guess a smaller or larger number,
have them choose an earlier or later word in the dictionary.
'''

import random

a = random.randint(0, 100)

def Numbercheck(x):
    try:
        str.isdigit(x)
    except ValueError as e:
        print('The input is not a number:', e)

    return int(x)


counter = 0

while counter != 3:
    str1 = input('guess the number of a\n')
    b = Numbercheck(str1)
    if b < a:
        print('too low')
        counter += 1

    elif b > a:
        print('too high')
        counter += 1
    else:
        print('correct number')



