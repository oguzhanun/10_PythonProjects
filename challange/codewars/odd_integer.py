def find_it(seq):
    odds = list()
    for i in seq :
        if i in odds :
            odds.remove(i)
        else :
            odds.append(i)

    return odds.pop()



print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))