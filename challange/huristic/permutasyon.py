nums = [1, 2,3,4,5]

set_nums = set(nums)

solution = [[]]

for index in range(len(nums)):
    solution = [i+[j] for i in solution for j in set_nums.difference(set(i))]


print(solution)

print([[5]+[3,4]])
