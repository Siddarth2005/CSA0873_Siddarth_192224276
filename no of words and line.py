string='''siddarth is great.siddu is innocent.sabarish is aggressive.'''
str1=string.split(".")
str1.pop()
print("no of lines in given para:",len(str1))
print("No of words in each line:")
for i in range(len(str1)):
    words=str1[i].split()
    print("line",i+1,len(words))
