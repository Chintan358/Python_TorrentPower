unit = int(input("enter unit : "))

total = 0;
if(unit<=100):
    total = unit*2
    print(f"Your bill is : {total}")
elif(unit>100 and unit <=200):
    total = unit*5
    print(f"Your bill is : {total}")
else:
    total = unit*10
    print(f"Your bill is : {total}")

