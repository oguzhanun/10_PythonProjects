# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses 
# the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers 
# and punctuation.

import string

def is_pangram(s):
    list_of_input=list(s.lower())
    list_of_pangram=list(string.ascii_lowercase)
    
    for i in list_of_input:
        if i in list_of_pangram:
            list_of_pangram.remove(i)
    
    if len(list_of_pangram) == 0 :
        return True
    else :
        return False

print(string.ascii_lowercase)

print(is_pangram("thequickbrownfxjmpsvelazydg"))

# ----------------
# import string

# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())


# ----------------

# import string

# def is_pangram(s):
#     s = s.lower()
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True