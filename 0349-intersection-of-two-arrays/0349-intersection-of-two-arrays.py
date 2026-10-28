class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        len1=len(nums1)
        len2=len(nums2)
        if len1<len2:
            for num in nums1:
                if num in nums2 and num not in result:
                    result.append(num)
        else:
            for num in nums2:
                if num in nums1 and num not in result:
                    result.append(num)
        return result