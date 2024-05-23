

class Student:
    id = 0
    name=""
    email=""

    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
    
    def __str__(self):
        return "Hello"

    def show(self):
        print(f"{self.id} - {self.name} - {self.email}")

s = Student(10,"Rahul","rahul@gmial.com")
s.show()
s1 = Student(11,'krunal','krunal@gmial.com')
s1.show()
print(s)
print(s1)