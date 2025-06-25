from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def  function1(piles,k,h):
            hours = 0

            for pile in piles:
                hours = hours + math.ceil(pile/k)

            if hours <= h:
                return True
            else:
                return False


        def function2(piles, h):
            low = 1
            high  = max(piles)
            ans = high

            while(low <= high):

                mid = (low + high) // 2

                if(function1(piles,mid,h) == True):
                    ans = mid
                    high = mid - 1
                else:
                    low  = mid + 1

            return ans
        return function2(piles,h)
        