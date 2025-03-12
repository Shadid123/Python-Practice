numberOfWords=0
numberOfDigits=0
numberOfLetters=0

text=input("Enter your text:")
for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        numberOfLetters=numberOfLetters+1
    elif x>='0' and x<='9':
        numberOfDigits=numberOfDigits+1
    elif x==' ':
        numberOfWords=numberOfWords+1    
            
print("Number of words:",numberOfWords+1)
print("Number of digits",numberOfDigits)
print("Number of letters",numberOfLetters)