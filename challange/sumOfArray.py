def sumOfArray(nums):
    maxSum = nums[0]
    temp = 0

    for i in range(len(nums)):
        temp += nums[i]
        if temp > maxSum :
            maxSum = temp

        if temp < 0 :
            temp = 0
    return maxSum

print(sumOfArray([-2,-1]))
