class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        size=len(nums)
        hash_map={0:1}
        result=0
        total=0
        for i in range(size):
                total+=nums[i]
                rem=total%k
                result+=hash_map.get(rem,0)
                hash_map[rem]=hash_map.get(rem,0)+1
        return result