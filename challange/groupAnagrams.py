# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

import collections

def groupAnagrams(strs) :
    

    # -----------------------------------------------

    # ans = collections.defaultdict(list)
    # for s in strs:
    #     ans[tuple(sorted(s))].append(s)
    # return ans.values()

    # -----------------------------------------------
    
    # anagram_set = set()
    
    # for i in strs :
        
    #     anagram_set.add(''.join(sorted(i)))
    
    # print("anagram set", anagram_set)

    # anagram_list = list(anagram_set)
    
    # output_list = list()
    
    # for i in range(len(anagram_list)):
    #     output_list.append([])
    
    # print("boşliste", output_list)

    # for i in strs :
    #     sorted_item = ''.join(sorted(i))
    #     index = anagram_list.index(sorted_item)
    #     output_list[index].append(i)

    # return output_list

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

