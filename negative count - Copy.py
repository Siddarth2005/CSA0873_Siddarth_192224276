a=[16, -18, 27, -16, 23, -21, 19]
result=[]
count=0
for i in a:
    if i<0:
        count+=1
        result.append(i)
print(result)
