class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
            
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if res > (MAX_INT - digit) // 10:
                return MAX_INT if sign == 1 else MIN_INT
                
            res = res * 10 + digit
            i += 1
            
        return sign * res
