

class Pen:
    
    price = 10
    color = "red"
    company = "cello"

    def __init__(self):
        print("pen init")

    def display(self):
        print(f"{self.price} - {self.color} - {self.company}")

class NoteBook(Pen):
    
    def __init__(self):
       super().__init__()
       

    pages = 100
    def show(self):
        print(f"{self.price} - {self.color} - {self.company} - {self.pages}")
    
# p = Pen()
# p.display()

# n = NoteBook()
# n.price = 500
# n.show()