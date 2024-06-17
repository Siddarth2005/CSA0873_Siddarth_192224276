k=int(input("Enter the no of digits:"))
n=int(input("Enter a number"))
s=n
l=len(str(n))
sum1=0
if(k==l):
    while n>0:
        r=n%10
        sum1=sum1+(r**l)
        n=n//10
    if s==sum1:
        print("armstrong number")
    else:
        print("Not a Armstrong number")
else:
    print("Invalid input")
