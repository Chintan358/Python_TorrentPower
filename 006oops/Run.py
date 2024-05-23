
class Test:

    def __init__(self):
        print("const calling")    

    def display(self):
        print("display calling..")

# t1 = Test()
# print(t1)
# t1.display()


class Sample:

    def __str__(self):
        return "Tops"
    

s1 = Sample()
print(s1)
