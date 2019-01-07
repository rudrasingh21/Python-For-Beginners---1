class Father():
    def gardening(self):
        print("I Enjoy Gardening")

class Mother():
    def cooking(self):
        print("I love Cooking")

class child(Father,Mother):     #Multiple Inheritance
    def sports(self):
        print("I Enjoy sports")

c = child()
#we can access from Father and Mother class , because we inherited

c.gardening()
c.cooking()
c.sports()