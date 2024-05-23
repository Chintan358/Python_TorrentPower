

# *
# **
# ***
# ****
# *****

lines = 5

# for i in range(1,lines+1):
#     for j in range(i):
#         print("*",end="")
#     print()

starcount = 1;
for i in range(1 , lines+1):
    for j in range(starcount):
        print("*",end="")
    starcount +=1
    print()

