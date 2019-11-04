# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:41:47 2019

@author: changyu
"""

def mysum(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum

print(mysum(1,2,3,4))

"""
Python的函数定义中有两种特殊的情况，即出现*，**的形式。
如：def myfun1(username, *keys)或def myfun2(username, **keys)等。

解释：
  * 用来传递任意个无名字参数，这些参数会一个Tuple的形式访问。
  **用来处理传递任意个有名字的参数，这些参数用dict来访问。
"""