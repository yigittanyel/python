class BankAccount:
    def __init__(self,name,money,age):
        self.name=name
        self.__money=money #private
        self.age=age
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self,amount):
        self.__money=amount
    
c1=BankAccount("Yigit", 1000, 20)
print("Bankadaki para:",c1.getMoney())
c1.setMoney(5000)
print("Yeni değer {}".format(c1.getMoney()))
