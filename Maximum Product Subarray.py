print("Maximum Product Subarray")

def function(nums):
    n = len(nums)
    leftmul = 1
    rightmul = 1
    maxmul = nums[0]
    for i in range(n):
        if (leftmul == 0):
            leftmul = 1
        if(rightmul == 0):
            rightmul = 1
        leftmul = leftmul * nums[i]

        j = n - i - 1
        
        rightmul = rightmul * nums[j]

        maxmul = max(maxmul, leftmul ,rightmul)

    return maxmul


nums = [1,2,-3,4]
print(function(nums))