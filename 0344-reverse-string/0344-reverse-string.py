class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap characters in-place
            s[left], s[right] = s[right], s[left]
            # Move pointers closer to the center
            left += 1
            right -= 1
