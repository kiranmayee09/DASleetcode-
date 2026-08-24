import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd = 0
        sumeven = 0

        for i in range(1, n + 1):
            sumodd += 2 * i - 1
            sumeven += 2 * i

        gcd = math.gcd(sumodd, sumeven)

        return gcd