class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #bits=k.bit_length()
        bits=0
        num=k
        while num:
            num//=2
            bits+=1
        res=0
        curr=0
        for i,c in enumerate(reversed(s)):
            if c=='0':res+=1
            else:
                curr+=(1<<i)
                if i<bits and curr<=k:res+=1
        return res
