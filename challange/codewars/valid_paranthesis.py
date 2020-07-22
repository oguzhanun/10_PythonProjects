# Write a function called that takes a string of parentheses, and determines if the order
# of the parentheses is valid. The function should return true if the string is valid, and 
# false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
# Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat 
# other forms of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
    opening = 0
    closing = 0
    for i in string :
        if i == "(" :
            opening += 1
        if i == ")" :
            closing += 1
        if closing > opening :
            return False
    if opening == closing :
        return True
    else :
        return False

print(valid_parentheses("dsaffa(sd)f"))