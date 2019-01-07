class Vehicle:
    def general_usage(self):
        print("General Use : transportation")

#sub class
class Car(Vehicle):     #i.e. Car class is inherited from vehicle class
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    #second method
    def specific_usage(self):
        print("specific usage is: for work, for family trip")

#second SUB CLASS
class MotorCycle(Vehicle):
    def __init__(self):
        print("I am MotorCycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("specific usage is: Racing")

#We have c & m object as instance of class Car() and MotorCycle()

c = Car()
c.general_usage()       #Using Inheritance
c.specific_usage()

m = MotorCycle()
m.general_usage()
m.specific_usage()

#NOTE:-
# Car class is derived from vehicle class
# We can see class->Car don't have method general_usage,
# but because of Inheritance class--> Car can access.


#************Other Way**************

#If you don't want to call c.general_usage()  method explicitly ,
# you can call them in specific_usage() methos as below.

#NOTE:- Same code with small change

class Vehicle:
    def general_usage(self):
        print("General Use : transportation")

#sub class
class Car(Vehicle):     #i.e. Car class is inherited from vehicle class
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    #second method
    def specific_usage(self):
        self.general_usage()        #Using Inheritance
        print("specific usage is: for work, for family trip")

#second SUB CLASS
class MotorCycle(Vehicle):
    def __init__(self):
        print("I am MotorCycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()        #Using Inheritance
        print("specific usage is: Racing")

#We have c & m object as instance of class Car() and MotorCycle()

c = Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()


# ************isinstance    &    issubclass methods************
#In next code