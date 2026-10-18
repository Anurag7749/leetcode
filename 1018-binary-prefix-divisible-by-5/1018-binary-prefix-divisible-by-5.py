class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = []
        num = 0

        for bit in nums:
            num = num * 2 + bit

            if num % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result