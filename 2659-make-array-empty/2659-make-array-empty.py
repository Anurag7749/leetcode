from typing import List

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        pos = {num: i for i, num in enumerate(nums)}
        nums.sort()
        operations = n
        
        for i in range(1, n):
            if pos[nums[i]] < pos[nums[i - 1]]:
                operations += n - i
                
        return operations
