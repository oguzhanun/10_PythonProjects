# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string 
# of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    
    print(*n)
    return f'({"".join(n[0:3])}) {"".join(n[3:6])}-{"".join(n[6:10])}'


print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

# x,y,z,t,f,s,r = 0

# stdTerminal10=[x,10]
# stdTerminal8 = [y, 8]

# diane = [1, z]

# charlie = [t, 9]

# alice = [x-1,f]

# bob = [s,r]

