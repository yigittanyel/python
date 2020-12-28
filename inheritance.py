# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:58:31 2020

@author: pc
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.gradyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.gradyear)

x = Student("Burak", "Aydın", 2018)
x.welcome()






