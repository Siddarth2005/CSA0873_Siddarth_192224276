n=int(input("Enter a number"))
s=n
l=len(str(n))
sum1=0
while n>0:
    r=n%10
    sum1=sum1+r
    n=n//10
print("The sum of digits is:",sum1)
