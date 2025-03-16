ch="Shadid"
vowel=int(0)
consonant=int(0)
for i in range(len(ch)):
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        vowel=vowel+1
    
    else :
        consonant=consonant+1
    
print("Vowel:",vowel)
    