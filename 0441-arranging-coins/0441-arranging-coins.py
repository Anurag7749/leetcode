class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        row=1
        while n>=row:
            n-=row
            count+=1
            row+=1
        return count