# Inheritance:

class Parent:
    def __init__(self, money):
        self.bank_balance = 200000
        self.car = "Honda City"
        self.childsPocketMoney = money

    def behaviour(self):
        print("Always having a smiling face")

class Child(Parent):
    def __init__(self, money):
        self.degree = "B.Ed"
        super().__init__(money)

sam = Child(500)

print(sam.degree)
print(sam.car)
sam.behaviour()
print(sam.childsPocketMoney)
