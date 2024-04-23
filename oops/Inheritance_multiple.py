class Rahul:
    r_id=""
    r_sub=""

    def r_setData(self):
        self.r_id = input("Enter Rahul id : ")
        self.r_sub = input("Enter rahul subject : ")


class Krunal:
    k_id=""
    k_sub=""

    def k_setData(self):
        self.k_id = input("Enter Krunal id : ")
        self.k_sub = input("Enter Krunal subject : ")

class Tops(Rahul,Krunal):

    def display(self):
        print("----Rahul Details----")
        print(" Id : ",self.r_id)
        print("Subject : ",self.r_sub)
        print("----Krunal Details----")
        print(" Id : ",self.k_id)
        print("Subject : ",self.k_sub)


t = Tops()
t.r_setData()
t.k_setData()
t.display()