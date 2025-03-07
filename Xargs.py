def add(*numbers):
    sum = 0
    for num in numbers:
        sum=sum+num
    print(f"Addition of {numbers} is:{sum}")
def sub(*numbers):
    sub=0
    for num in numbers:
        sub=sub-num
    print(f"Substraction of {numbers} is:{sub}")
def mul(*numbers):
    mul=1
    for num in numbers:
        mul=mul*num
    print(f"Multiplication of {numbers} is:{mul}")
def div(*numbers):
    div=numbers[0]
    for num in numbers[1:]:
        div=div//num
    print(f"Division of {numbers} is:{div}")

add(10,20,30)
sub(10,20)
mul(10,30)
div(30,2,2)

