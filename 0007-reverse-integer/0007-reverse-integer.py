class Solution:
    def reverse(self, x: int) -> int:

        sign = 1
        if x < 0:
            sign = -1
            x = -x
        reverse = 0

        while x != 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x//10
        reverse = sign * reverse
        if reverse < -2**31 or reverse > 2**31 -1:
            return 0
        return reverse

