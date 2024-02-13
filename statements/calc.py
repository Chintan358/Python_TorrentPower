a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter choice : \n 1 - add \n 2 - sub \n 3 - div \n 4 - mul"))

if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a/b)
elif(c==4):
    print(a*b)
else:
    print("invalid choice")