class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def function1(weights,capacity,days):
            req_days = 1
            curr_wight = 0
            for weight in weights:
                if(curr_wight + weight <= capacity):
                    curr_wight  = curr_wight + weight
                else:
                    req_days += 1
                    curr_wight = weight
    
            if req_days <= days:
                return True
            else:
                return False



        def function2(weights,days):
            low = max(weights)
            high = sum(weights)
            ans = high
            while(low <= high):
                mid = (low + high) // 2
                if(function1(weights,mid,days) == True):
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        return function2(weights,days)
        