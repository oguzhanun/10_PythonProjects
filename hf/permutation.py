def who_goes_free(n, k):
    prisinors = list(range(n))
    k -= 1
    kill_s = k
    if n == 1:
        print(1)
    else:
        while len(prisinors) > 1:
            prisinors.pop(kill_s)
            kill_s = (kill_s + k) % len(prisinors)
            print(prisinors)
        print('survivor: ', prisinors[0])


n = int(input(": "))
k = int(input(": "))
who_goes_free(n, k)

