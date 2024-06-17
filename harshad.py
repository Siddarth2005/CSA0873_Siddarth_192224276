n=int(input("Enter a number"))
s=n
l=len(str(n))
sum1=0
while n>0:
    digit=n%10
    sum1=sum1+digit
    n=n//10
if(s%sum1==0):
    print("Harshad number")
else:
    print("Not a harshad number")
