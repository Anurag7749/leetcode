class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s="".join(ch.lower() for ch in s if ch.isalnum())
        def check_palindrome(low:int,high:int)->bool:
            if low>=high:
                return True
            if new_s[low]!=new_s[high]:
                return False
            return check_palindrome(low+1,high-1)
        return check_palindrome(0,len(new_s)-1)