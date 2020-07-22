def happyNumber(i):
    l1= list()
#    l1.append(i)

    while True :
    
        a = list(str(i))
        print(a)
        c = 0
    
        for b in a :
            print("for döngüsü : ", b)
            c += int(b)**2
        
        print(c)
        i = c
        
        if c == 1:
            print(True)
            return True
            break
        elif c not in l1:
            l1.append(c)
        else :
            print(False)
            return False

happyNumber(input("enter an integer :"))


    