class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        i = 0
        sign = 1
        result = 0
        
        # Handle sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Process digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Overflow check BEFORE adding digit
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            i += 1
        
        return sign * result