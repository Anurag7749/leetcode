class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum=0
        digit_sum=0
        for i in range(len(nums)):
            element_sum+=nums[i]
        for i in range(len(nums)):
            while(nums[i]!=0):
                sum=nums[i]%10
                digit_sum+=sum
                nums[i]=nums[i]//10
        return abs(element_sum-digit_sum)
        