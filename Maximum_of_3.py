num1=int(20)
num2=int(110)
num3=int(90)
if num1==num2 and num1==num3:
    print("All are equal")
else:
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2>num3:
        print(num2)
    else:
        print(num3)