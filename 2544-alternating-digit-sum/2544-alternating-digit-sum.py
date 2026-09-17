class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """ ans = 0
        sign = 1

        for digit in str(n):
            ans += sign * int(digit)
            sign = -sign

        return ans 

        ans = 0

        for i, digit in enumerate(str(n)):
            if i % 2 == 0:
                ans += int(digit)
            else:
                ans -= int(digit)

        return ans """

        s = str(n)

        positive = sum(int(x) for x in s[::2])
        negative = sum(int(x) for x in s[1::2])

        return positive - negative