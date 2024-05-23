

class GarndParent:
    car="swift"
    def __init__(self,car):
        self.car = car

class Parent(GarndParent):
    home="flat"
    def __init__(self,home):
        self.home = home

class Child(Parent):
    bike=""
    def __init__(self,bike):
        self.bike = bike

    def myProp(self):
        print(f"{self.car} : {self.home} : {self.bike}")



g = GarndParent("Swift")
p = Parent("flat")
c = Child("Suzuki")
c.myProp()