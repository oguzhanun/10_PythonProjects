# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers 
# according to the following pattern:
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in 
# this kata.
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same 
# pattern shown above.
# For example, decode("h3 th2r2") would return "hi there".
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to 
# vowels.
# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

vowel_code = {"a":"1","e":"2","i":"3","o":"4","u":"5"}  # join function does not accept integer...

def encode(st):
    L = list()
    for i in st:
        if i not in vowel_code.keys():
            L.append(i)
        else:
            L.append(vowel_code.get(i))
    return "".join(L)
    
def decode(st):
    L = list()
    for i in st:
        if i not in vowel_code.values():
            L.append(i)
        else:
            a=list(vowel_code.keys())
            index=int(i)-1
            L.append(a[index])
    return "".join(L)

print(encode("hello"))
print(decode("h2ll4"))



# *********** OTHERS CODE ***********

# def encode(st):
#     return(st.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5"))
    
# def decode(st):
#     return(st.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u"))