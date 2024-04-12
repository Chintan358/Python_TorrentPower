
class Pen:
    price = 10
    company="cello"
    color = "blue"

    def display(self):
        print("Runing display")
        print(f"{self.price} - {self.company} - {self.color}")


p = Pen()
p.price=50
p.display()

print("******************")

p1 = Pen()
p1.price=100
p1.display()
