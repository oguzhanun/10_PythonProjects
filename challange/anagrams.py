# What is an anagram? Well, two words are anagrams of each other if they both contain 
# the same letters. For example:

# 'abba' & 'baab' == true

# 'abba' & 'bbaa' == true

# 'abba' & 'abbba' == false

# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two 
# inputs a word and an array with words. You should return an array of all the anagrams or an empty
#  array if there are none. For example:

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
z = list()

def recur(x, words, words_list):
    
    if x >= 0:
        if sorted(words) == sorted(words_list[x]) :
            z.append(words_list[x])
        return recur(x-1,words,words_list)
    else :
        return z

    
    # output = list()

    # for i in words_list :
    #     if sorted(word) == sorted(i):
    #         output.append(i)
    # return output

print(recur(3,'abba', ['aabb', 'abcd', 'bbaa', 'dada']))