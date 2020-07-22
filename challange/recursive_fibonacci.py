# fibonacci sayıları 1,1,2 serisi ile başlar ve bir sonraki rakam kendinden önceki iki rakamın toplamıyla
# bulunur.
i = 2

def fibo(x) :
    if x <= 0 :
        return 0
    if x == 1 :
        return 1 
    if x == 2 :
        return 2
    if x > 2 :
        #i = i+1
        return (fibo(x-1) + fibo(x-2)) 
z = list()

def serial_fibo(x) :
    
    for i in range(x):
        z.append(fibo(i))
    return z

print(serial_fibo(9))

t = [1,1]
def fibo_serial(x,i=1) :
    if x < 2 :
        return [1]
    if i <= x and x >= (t[i] + t[i-1]):
        t.append(t[i] + t[i-1])
        i = i + 1
        return fibo_serial(x,i)
    else :
        return t

print(fibo_serial(2))
