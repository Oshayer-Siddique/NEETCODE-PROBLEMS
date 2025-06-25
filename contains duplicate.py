def function(nums):
    n = len(nums)
    arr = set(nums)
    if len(arr) == len(nums):
        return False
    else:
        return True

    

print(function(nums=[1,1,1,3,3,3,4,4]))