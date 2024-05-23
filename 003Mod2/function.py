

def test():
    print("Test function callaing")

test()



def add(a,b):
    print(a+b)

add(10,20)


def square(a):
    return a*a

sq=square(10)
print(sq)

def student(name,id=10,email="test@gmail.com"):
    print(f"id of student is {id} and name is {name}")

student("Rahul")

def setdata(a,b):
    print(f"a : {a}")
    print(f"b : {b}")
setdata(b=20,a=10)

def mydata(*tpl):
    print(tpl)

mydata(10,20,30,40,50)

def empdata(**dict):
    print(dict)
empdata(name="Rahul",email="rahul@gmail.com")

k = lambda : print("Hello")   
k()

y = lambda a,b:print(a+b) 
y(10,20)


x = lambda *a:print(a)
x(10,20,30,40,50,60)