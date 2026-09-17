class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        sign = 1

        for digit in str(n):
            ans += sign * int(digit)
            sign = -sign

        return ans