# https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python


def convertFracts(lst):
    if lst != [] :
        denominator = 1
        share = list()

        for i in lst :
            denominator *= i[1]
            share_elem = i[0]
            for t in range(len(lst)):
                if lst.index(i) != t :
                    share_elem *= lst[t][1]
            share.append(share_elem)
        while (denominator % 2 == 0 and len([i for i in share if i%2==0]) == len(share) ) or (denominator % 3 == 0 and len([i for i in share if i%3==0]) == len(share) ) or (denominator % 5 == 0 and len([i for i in share if i%5==0]) == len(share) ):
            if denominator % 2 == 0 and len([i for i in share if i%2==0]) == len(share) :
                denominator=denominator / 2
                for i in range(len(share)) :
                    share[i] /= 2 
            elif denominator % 3 == 0 and len([i for i in share if i%3==0]) == len(share) :
                denominator=denominator / 3
                for i in range(len(share)) :
                    share[i] /= 3
            else:
                denominator=denominator / 5
                for i in range(len(share)) :
                    share[i] /= 5 
        for i in range(len(lst)) :
            for t in range(len(lst[i])) :
                if t == 0:
                    lst[i][t] = share[i]
                else:
                    lst[i][t] = denominator
        return lst
    else :
        return [] 
    
print(convertFracts([[1,3],[1,4],[1,6],[1,12]]))




# ------------------------------

# def convertFracts(lst):
#     e = 1
#     for i in lst:
#         e = lcm(e, i[1])
#     return [[int(e/i[1])*i[0], e] for i in lst]
    
# def gcd(a,b): 
#     if a == 0: 
#         return b
#     return gcd(b % a, a) 
    
# def lcm(a,b): 
#     return (a*b) / gcd(a,b)