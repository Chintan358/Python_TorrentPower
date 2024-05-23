
marks = int(input("enter marks : "))

if(marks>90 and marks<=100):
    print("grade A")
elif(marks>70 and marks<=90):
    print("grade B")
elif(marks>50 and marks<=70):
    print("grade C")
elif(marks>35 and marks<=50):
    print("grade D")
elif(marks>0 and marks<=35):
    print("grade F")
else:
    print("invald marks")
