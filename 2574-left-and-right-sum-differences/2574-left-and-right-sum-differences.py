class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftsum=[0]*n
        rightsum=[0]*n
        answer=[0]*n
        for i in range(n-1):
            leftsum[i+1]=leftsum[i]+nums[i]
        for i in range(n-2,-1,-1):
            rightsum[i] = rightsum[i+1] + nums[i+1]   
        for i in range(n):
            a=abs(leftsum[i]-rightsum[i])
            answer[i]=a
        return answer