

dict = {};
def addQuesions():

    num = int(input("How many questions do you want to enter : "))
    for i in range(num) : 
        que = input("Enter question : ")
        a =input("enter option 1 : ")
        b = input("enter option 2 : ")
        c = input("enter right ans : ") 

        abc = {que : {"A":a,"B":b,"Right answer":c}}
        dict.update(abc)
  

def viewQuestions():
    for x ,obj in dict.items():
        print(x)

        for y in obj:
            print(y +" : ", obj[y])
            

def deleteQuestions():
    que  = input("enter question : ")
    dict.pop(que)