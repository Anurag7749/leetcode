class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
        for j in range(len(t)):
            if t[j] in stack:
                stack.remove(t[j])
            else:
                return t[j]