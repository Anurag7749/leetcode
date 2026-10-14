class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map={0:-1}
        count=0
        max_length=0
        size=len(nums)
        for i in range(size):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            if count in hash_map:
                length=i-hash_map[count]
                max_length=max(length,max_length)
            else:
                hash_map[count]=i
        return max_length