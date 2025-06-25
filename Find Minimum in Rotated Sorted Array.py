print("Find Minimum in Rotated Sorted Array")


nums = [4,5,6,7]

def function(nums):
    low = 0
    high = len(nums) - 1
    

    while(low < high):
        mid = (low + high) // 2
        if(nums[mid]  > nums[high]):
            
            low = mid + 1
        else:
            high = mid
    return nums[low]


print(function(nums))

