def inner_work(lst):
    z = list()
    i=0
    t=0
    f=len(lst)
    while i<f :
        t=i
        while t<f+i :
            a=lst.pop(t%f)
            lst.insert((t+1)%f,a)
            z.append(lst.copy())  # if .copy() function is not used, I can't make it a deep copy although 
                                  # .copy() function should make a shallow copy...
            t = t + 1
        i = i + 1  
    k = list()
    for v in z :
        counter1=0
        counter2=0
        valid=True
        for x in v :
            if x=="(":
                counter1=counter1+1
            else :
                counter2=counter2+1
            if counter2 > counter1 :
                valid=False
                break
        if valid :
            k.append("".join(v))
    return k
def parantheses(length_of_parantheses) :
    lst1 = list("()" * length_of_parantheses)
    lst2 = list("(" * length_of_parantheses + ")" * length_of_parantheses)
    return set(inner_work(lst1)).union(set(inner_work(lst2)))
print(parantheses(10))

