
#     *
#    ***
#   *****
#  *******
# *********

lines = 5;
for i in range(1,lines+1):
    for k in range(lines-i):
        print(" ",end="")
    for j in range(i+(i-1)):
        print("*",end="")
    print()

