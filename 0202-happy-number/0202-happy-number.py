class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)

            total = 0
            x = n

            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            
            n = total

        return True