
# *****
# ****
# ***
# **
# *


# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

starCount = 5;
for i in range(5,0,-1):
    for j in range(starCount):
        print("*",end="")
    starCount -=1
    print()