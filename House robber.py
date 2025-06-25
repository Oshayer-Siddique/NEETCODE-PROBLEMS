print("House Robber")


# def function(nums):
#     n = len(nums)
#     if n == 1:
#         return nums[0]
#     elif n == 2:
#         return max(nums[0] , nums[1])
#     else:
#         return max(nums[n-1]+function(nums[:n-2]), function(nums[:n-1]))
    




def function(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    

    loots = [0 for i in range(n+1)]
    loots[0] = 0
    loots[1] = nums[0]
    
    for i in range(2,n+1,+1):
        loots[i] = max(nums[i-1] + loots[i-2], loots[i-1])
    return loots[n]


nums = [2,9,8,3,6]

print(function(nums))
    