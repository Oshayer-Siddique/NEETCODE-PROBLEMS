nums = [3,4,5,6,1,2]

def function(nums):
    low = 0
    high = len(nums) - 1
    
    while(low < high):
        mid = (low+high)//2
        if(nums[mid] > nums[high]):
            
            low = mid + 1
        else:
            high = mid
    return nums[low]


def function2(nums):
    low = 0
    high = len(nums)-1
    while(low < high):
        mid = (low + high)//2
        if(nums[mid] > nums[high]):
            low = mid
        else:
            high = mid - 1
        # if(low + 1 == high):
        #     return max(nums[low],nums[high])
    return nums[low]


print(function(nums))
print(function2(nums))

