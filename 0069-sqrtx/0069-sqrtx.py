import math

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        # Keep going up while the next number squared is less than or equal to x
        while (i + 1) * (i + 1) <= x:
            i += 1
        return i