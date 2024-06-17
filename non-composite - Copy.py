array=[2,4,3,18,17,24,28]
result=[]
for num in array:
    if num<2:
        continue
    count=0
    for i in range(2,num):
        if(num%i==0):
            count+=1
    if(count==0):
        result.append(num)
print(result)
            
