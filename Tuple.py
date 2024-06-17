Lower_range=int(input("enter Lower range:"))
Upper_range=int(input("Enter Upper range:"))
if(Lower_range>Upper_range):
    print("Invalid Input")
else:
    result=[(num,num**2)for num in range(Lower_range,Upper_range+1)]
    print(result)
