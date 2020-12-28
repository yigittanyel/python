# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 02:09:14 2020

@author: pc
"""

# def func1():
#   a = "Deneme"
#   print(a)
# func1()

# a= 700
# def func1():
#   a = 200
#   print(a)
# func1()  #200
# print(a) #300

a=700
def func1():
  global a
  a= 200
func1()
print(a) #200

