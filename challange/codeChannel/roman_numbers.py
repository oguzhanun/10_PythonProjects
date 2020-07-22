# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# -----------------------------------------------------------------------
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
# Example 1:
# Input: 3
# Output: "III"
# Example 2:
# Input: 4
# Output: "IV"
# Example 3:
# Input: 9
# Output: "IX"
# Example 4:
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



def translate_to_roman(num):
    
    str_of_num = list(str(num))[::-1]
    nodes = list()
    roman_num = list()
    
    for i in range(len(str_of_num)) :
        nodes.append(10**i * int(str_of_num[i]))
    
    print("NODES:",nodes)
    
    for i in nodes :
        if i < 10 :
            if i < 4 :
                roman_num.append(i*"I")
            elif i == 4 :
                roman_num.append("IV")
            elif 5 <= i < 9 :
                roman_num.append("V" + "I"*(i-5))
            else :
                roman_num.append("IX")

        if 10 <= i < 100 :
            if i < 40 :
                roman_num.append("X"*(i//10))
            elif i == 40 :
                roman_num.append("XL")
            elif 50 <= i < 90 :
                roman_num.append("L" + "X"*(i//10-5))
            else :
                roman_num.append("XC")

        if 100 <= i < 1000 :
            if i < 400 :
                roman_num.append("C"*(i//100))
            elif i == 400 :
                roman_num.append("CD")
            elif 500 <= i < 900 :
                roman_num.append("D" + "C"*(i//100-5))
            else :
                roman_num.append("CM")

        if 1000 <= i < 4000 :
            roman_num.append("M"*(i//1000))
    
    roman_num = roman_num[::-1]
    print("ROMAN_EQUALENT:", roman_num)
    
    return "".join(roman_num)

print(translate_to_roman(3850))


def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman

print("convert: ",convert(3850))

seen = [[] for _ in range(4 + 1)]

print(seen)