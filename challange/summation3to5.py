
def summation(number):
    B = sum(set(range(0,int(number)+1,3)) | set(range(0,int(number)+1,5)))
    c = sum(set(range(5)) | set(range(6)))
    print("c", c)
    print(B)


summation(15)


