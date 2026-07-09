class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit

        num += 1

        result = []

        if num == 0:
            return[0]
        
        while num > 0:
            result.append(num % 10)
            num //= 10

        result.reverse()
        return result