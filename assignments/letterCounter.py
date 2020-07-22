sentence = input("please give me a string")

dict1 = dict()

for i in sentence :
    if i in dict1.keys():
        dict1[i]=dict1[i]+1
    else :
        dict1[i]=1

print(dict1)