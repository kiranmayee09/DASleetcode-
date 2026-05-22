class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        sum = 0
        for i in range(n):
            sum ^= start + 2 * i
        return sum