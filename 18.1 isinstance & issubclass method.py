# ************isinstance    &    issubclass methods************

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
m = MotorCycle()

print(isinstance(c,Car))
print(isinstance(c,MotorCycle))

print(isinstance(m,Car))
print(isinstance(m,MotorCycle))

print(issubclass(Car,Vehicle))

# Will give you output as True and False

#NOTE:- isinstance
# Will tell if an object is instance of a specific class or not

