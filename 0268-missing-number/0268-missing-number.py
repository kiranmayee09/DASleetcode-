class Solution(object):
    def missingNumber(self, nums):
        
        n = len(nums)
        xor1 = 0
        xor2 = 0

        for i in range(n+1):
            xor1 ^= i

        for num in nums:
            xor2 ^= num

        return xor1 ^ xor2