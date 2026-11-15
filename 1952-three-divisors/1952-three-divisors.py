import math

class Solution:
    def isThree(self, n: int) -> bool:
        root = math.isqrt(n)
        if root * root != n or root < 2:
            return False
        for i in range(2, math.isqrt(root) + 1):
            if root % i == 0:
                return False
        return True
