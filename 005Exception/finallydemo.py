
def printdata():
    try:
        num =int(input("enter number : "))
        return 1;
    except Exception as e:
        return 0
    finally:
        print("Hello py")


n = printdata()
print(n)
