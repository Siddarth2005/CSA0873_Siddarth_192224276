arr=[0,4,1,2,2,1,0,3,4]
arr.sort()
print(arr)
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
