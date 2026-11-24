class Solution:
    def isPalindrome(self, s: str) -> bool:
        new="".join(ch.lower() for ch in s if ch.isalnum())
        n=len(new)
        low=0
        high=n-1
        while low<high:
            if new[low]!=new[high]:
                return False
            else:
                low+=1
                high-=1
        return True
         