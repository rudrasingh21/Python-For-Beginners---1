class Father():
    def skills(self):
        print("Programming, Gardening")

class Mother():
    def skills(self):
        print("Art, Cooking")

class child(Father,Mother):     #Multiple Inheritance
    def skills(self):
        print("Sports")

c = child()
#we can access from Father and Mother class , because we inherited

c.skills()  #it will only print "Sports"

#******************Other Way -- Inheritance***********

class Father():
    def skills(self):
        print("Programming, Gardening")

class Mother():
    def skills(self):
        print("Art, Cooking")

class child(Father,Mother):     #Multiple Inheritance
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c = child()
#we can access from Father and Mother class , because we inherited

c.skills()
'''
OUTPUT:-
Programming, Gardening
Art, Cooking
Sports
'''