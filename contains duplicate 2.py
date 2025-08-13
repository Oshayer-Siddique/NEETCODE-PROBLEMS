def function(nums, k):
            n = len(nums)
            window = set()
            for i in range(n):
                if nums[i] in window:
                    return True
                window.add(nums[i])

                if len(window )> k:
                    window.remove(nums[i-k])
            
            return False

