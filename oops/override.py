
class A:
    def sample(self):
        print("class A sample calling")


class B(A):
     def sample(self):
        print("class B sample calling")

a = A()
a.sample()

b = B()
b.sample()