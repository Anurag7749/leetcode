class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result={}
        for num in nums:
            result[num]=1+result.get(num,0)
        return max(result, key=result.get)