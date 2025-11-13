class Car:
    name =  None
    price = None
    color = None
    def __init__(self,name,price,color):
        self.set_data(name,price,color)
        self.get_data()
    def set_data(self, name = None, price = None, color = None):
        self.name = name
        self.price = price
        self.color = color

    def get_data(self, name=None, price=None, color=None):
        self.name = name
        self.price = price
        self.color = color
carOne = Car("one",1,"red")
carTwo = Car("two",2,"blue")
print(carOne)
print(carTwo)
# carOne.set_data("BWM", 90000, "red")
# carTwo = Car("Audi", 90000, "red")
# print(carTwo.get_data())
# carOne.name = "BMW"
# carOne.price = 50000
# carOne.color = "red"
# carTwo = Car()
# carTwo.name = "Audi"
# carTwo.price = 70000
# carTwo.color = "blue"
carOne.set_data
carTwo.get_data()

# from mymodule import addNumbers as addN
#
# print(addN(20,30,0))

# import mymodule as my
#
# print(my.name)
# my.findName()
# import datetime as dt
# from math import sqrt as sq, ceil as ceil
# print(ceil(sq(99)))

# import datetime as dt
# Просисываем псевдоним dt от datatime
# import datetime as dt, sys, os, platform
# time.sleep(1)

# print(dt.datetime.now().date())
# print(dt.datetime.now().time())
# print(sys.platform)
# print(sys.path)
# print(os.name)
# print(platform.system())