class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        original = n
        summ = 0
        product = 1

        while n > 0:
            digit = n % 10

            summ += digit
            product *= digit

            n //= 10

        return original % (summ + product) == 0