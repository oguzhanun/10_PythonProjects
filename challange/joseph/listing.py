
x=[([1], [2, 3], (4, 5, 6))]
set1=set()

for i in x[0] :
    for t in i :
        set1.add(t)

print(t)



print(set([z for i in x[0] for z in i]))