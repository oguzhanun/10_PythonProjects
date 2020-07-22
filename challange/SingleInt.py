
def singleNumber( nums) :
    
    for i in nums :

        nums.remove(i)
        
        if i not in nums :
            nums.append(i)
            print("answer:",i)
            return i
        else :
            nums.append(i)
            

i = singleNumber([4,1,2,1,2,5,5])

print("sonuc",i)
