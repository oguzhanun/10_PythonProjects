word=input(str("Enter a word: "))

dic={}
for i in word:
    dic[i]=dic.get(i,0)+1  # if get method can't find the key it returns 0 
print(dic)