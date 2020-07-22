

def maxSubArray(liste):
    
    b = 0
    a = 0
    if len(liste) == 1 :
        return liste[0]
    else:
        
        a = a + liste[0] + maxSubArray(liste[1:])
        print("a",a)
        if(a > b):
            b = a
            print("b", b)
        return b

a = 0
b = 0
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))