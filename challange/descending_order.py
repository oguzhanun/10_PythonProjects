# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 21445 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num) :

    #num = sorted(str(num),)
    number = list(str(num))
    number.sort(reverse=True)
    result = ""
    for i in number :
        result= result + i

    return int(result)


print(-5/2)



print(descending_order(2019384668362))