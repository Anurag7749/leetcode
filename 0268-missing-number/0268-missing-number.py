class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans=0
        hash_map=[]
        for i in range(len(nums)):
            hash_map.append(nums[i])
        for j in range(len(nums)+1):
            if j not in hash_map:
                ans=j
        return ans
