print("House Robber 2")



nums = [2,9,8,3,6]

n = len(nums)

nums1 = nums[:n-1]
nums2 = nums[1:n]

def oldfunction(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    loots = [0 for i in range(n+1)]
    loots[0] = 0
    loots[1] = nums[0]
    for i in range(2,n+1,+1):
        loots[i] = max(nums[i-1]+loots[i-2] , loots[i-1])
    return loots[n]

def newfunction(nums1,nums2):
    return max(oldfunction(nums1), oldfunction(nums2))

print(newfunction(nums1,nums2))

