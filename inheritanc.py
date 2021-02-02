class Website:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
        print("Website is created")
    def login(self):
        print(self.name+" "+str(self.age))

class Webs2(Website):
    def __init__(self, name, age, ids):
        Website.__init__(self,name,age)
        self.ids=ids
        print("Website 2 is created")
        
    def log(self):
        print(self.name+" "+str(self.age)+str(self.ids))

w1=Website("Yigit",20)
w1.login()
w2=Webs2("Semih",9,7)
w2.log()