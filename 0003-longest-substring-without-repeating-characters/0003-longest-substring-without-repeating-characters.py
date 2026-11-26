class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        best=0
        last_seen={}
        for right,character in enumerate(s):
            if(character in last_seen and last_seen[character]>=left):
                left=last_seen[character]+1
            last_seen[character]=right
            current_length=right-left+1
            best=max(best,current_length)
        return best

