
class Calc:

    
    

    # def add(self,a,b,c):
    #     self.a = a
    #     self.b = b
    #     self.c = c
    #     print(self.a+self.b+self.c)
    
    # def add(self,a,b):
    #     self.a = a
    #     self.b = b
    #     print(self.a+self.b)

    def add(self,*args):
        sum = 0
        for i in args:
            sum = sum +i
        print("sum : ",sum)

    def data(self,*args):
        print(args)

c  =Calc()
c.add(10,20)
c.add(10,20,30,56)
c.add(10,23,69,45,89,96)
c.data(10)
c.data(20,"Rahul",10.23,'a')