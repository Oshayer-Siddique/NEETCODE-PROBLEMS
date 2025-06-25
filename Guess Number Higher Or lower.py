# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

from typing import List
import math


# Mock guess API for local testing
picked_number = 0  # Set this to the number you want to "pick" for testing

def guess(num: int) -> int:
    if num > picked_number:
        return -1
    elif num < picked_number:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int):
        low , high = 1,n
        while(low <= high):
            mid = (low + high) // 2
            ans = guess(mid)
            if(ans == -1):
                high = mid - 1
            elif(ans == 1):
                low = mid + 1
            else:
                return mid
        
        