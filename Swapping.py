a=10
b=20
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)

a=30
b=50
a,b=b,a
print("a=",a)

print("a=",b)