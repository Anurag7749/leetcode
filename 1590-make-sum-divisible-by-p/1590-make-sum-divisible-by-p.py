class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
            
        if total % p == 0:
            return 0
        else:
            rem = total % p
            min_len = n
            curr_rem = 0
            seen = {0: -1}
            
            for i in range(n):
                curr_rem = (curr_rem + nums[i]) % p
                needed_rem = (curr_rem - rem + p) % p
                
                if needed_rem in seen:
                    min_len = min(min_len, i - seen[needed_rem])
                    
                seen[curr_rem] = i
                
            return min_len if min_len < n else -1
