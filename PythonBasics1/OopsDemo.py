class Calculator:
    num=100
    #Constructor
    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("I'm called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


ob = Calculator(2, 3)# syntax to create objects in python
ob.getData()
print(ob.Summation())