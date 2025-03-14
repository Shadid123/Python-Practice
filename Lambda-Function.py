GivenNumber=int(input("Enter a number:"))

cube=lambda x: x*x*x

print(f"Square of {GivenNumber} is:",(lambda x:x*x) (GivenNumber))
print(f"Cube of {GivenNumber} is:", (lambda x:x*x*x) (GivenNumber))


