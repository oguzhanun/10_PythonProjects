from random import randint

def who_dies(n,k) :
    prisoner = list(range(n))
    
    m = randint(0,n-1)

    if(n == 1) :
        return prisoner[0]
    else:
        while len(prisoner) > 1 :
            prisoner.pop(m)
            m = (m + k -1) % len(prisoner)
    return prisoner[0]

n = int(input("enter the number of prisoners"))
k = int(input("enter the number of steps :"))
print(who_dies(n,k))


def who_goes_free(n,k):
    return 0 if n==1 else (who_goes_free(n-1, k) + k) % n

print(who_goes_free(n,k))