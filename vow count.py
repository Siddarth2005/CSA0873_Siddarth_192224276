str = input("Enter the string:")
vcount, ccount= 0,0
Vowels = "AaEeIiOoUu"
c=[]
v=[]
str = str.lower()
for i in range(0,len(str)):
    if str[i] in (Vowels):
        vcount = vcount + 1
        v.append(str[i])
    elif (str[i] not in (Vowels)):
        ccount = ccount + 1
        c.append(str[i])
print("Total number of vowel and consonant are" )
print("vowels in the given string:",v)
print("Number of vowels:",vcount)
print("consonants in the given string:",c)
print("Number of consonants:",ccount) 
