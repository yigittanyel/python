# -*- coding: utf-8 -*-

# class Player:
#   def __init__(self, name, age,position):
#     self.name = name
#     self.age = age
#     self.position=position
    
#   def printPlayer(self):
#     print("Name: " + self.name+" "+"Age: "+str(self.age)+" "+"Position: "+self.position)

# p1 = Player("Ali", 32,"Middle")
# p2=Player("Mehmet",27,"Goalkeaper")
# p1.printPlayer()
# p2.printPlayer()

class Player:
  def __init__(self, name, age,position):
    self.name = name
    self.age = age
    self.position=position
    
  def printPlayer(self):
    print("Name: " + self.name+" "+"Age: "+str(self.age)+" "+"Position: "+self.position)

class substitute(Player):
  def __init__(self, name, age,position):
    super().__init__(name, age,position)

x = substitute("Ahmet",19,"Forward")
x.printPlayer()














