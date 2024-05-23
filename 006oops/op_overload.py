
class Point:  
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} , {self.b}";
    
    def __mul__(self,other):
        a = self.a*other.a 
        b = self.b*other.b
        return Point(a,b)
    
    def __add__(self,other):
        a = self.a+other.a 
        b = self.b+other.b
        return Point(a,b)

p1 = Point(10,20)
p2 = Point(20,40)

print(p1)
print(p2)
print(p1*p2)
print(p1+p2)