

def test():
    print("Test function callaing")

def add(a,b):
    print(a+b)

def square(a):
    return a*a

def student(name,id=10,email="test@gmail.com"):
    print(f"id of student is {id} and name is {name}")


def setdata(a,b):
    print(f"a : {a}")
    print(f"b : {b}")




test()
add(10,20)
sq=square(10)
print(sq)
student("Rahul")
setdata(b=20,a=10)
