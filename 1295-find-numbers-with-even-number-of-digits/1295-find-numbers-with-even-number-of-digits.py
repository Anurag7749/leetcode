class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            # Convert the number to a string and check if its length is even
            if len(str(num)) % 2 == 0:
                count += 1
        return count
