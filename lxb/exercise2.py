#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
*re-implementing functionality*
The function takes a sequence of numbers, and returns the sum of those numbers. so if you were to invoke
sum([1,2,3]), the result would be 6.

The challenge here is to write a mysum function that does the same thing as the built-in sum function.
However, instead of taking a single sequence.

(The built-in sum function takes an optional second argument, which we're ignoring here.)

(And in particular, you should think about the types of parameters functions can take in Python.
In many languages, functions can be defined multiple times, each with a different type signature (i.e.
number of parameters, and parameter types). In Python, only one function definition
i.e., the last time that the function was defined) sticks. The flexibility comes from appropriate use of
the different parameter types.)

[arbitrary-argument-lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)

'''



def mysum(numberlist):
    sum1 = 0
    for ele in numberlist:
        sum1 += ele
    return sum1

NumList = []
n = 0
while n <= 5:
    x = int(input('Please input a number in the list\n'))
    NumList.append(x)
    n += 1

mysum(NumList)
print(mysum(NumList))