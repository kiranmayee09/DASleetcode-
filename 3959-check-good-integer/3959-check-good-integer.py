class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0

        for digit in str(n):
            digit = int(digit)

            digitSum += digit
            squareSum += digit ** 2

        return squareSum - digitSum >= 50