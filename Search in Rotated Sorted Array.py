def function(nums,target):
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            return mid
        if(nums[low] <= nums[mid]):
            if(nums[low] <= target <nums[mid]):
                high = mid - 1
            else:
                low = mid + 1

        else:
            if(nums[mid] <target <= nums[high]):
                low = mid + 1
            else:
                high = mid - 1
    return -1

nums=[3,4,5,6,1,2]
target=1
print(function(nums, target)) 