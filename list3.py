# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:41:10 2019

@author: Administrator
"""

list1=[6,5,9]
list2=[0,4,2,1]
list1.extend(list2)
print(list1)
list2.insert(2,45)
print(list2)
list1.pop()
print(list1)
print(list1.count(0))
list1.clear()
print(list1)
list1=list2.copy()
print(list2)
print(list1.index(45))
list1.sort()
print(list1)

