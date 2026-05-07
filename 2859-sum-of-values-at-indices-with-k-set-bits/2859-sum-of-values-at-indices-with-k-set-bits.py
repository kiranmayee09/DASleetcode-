class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            binary = bin(i)[2:]
            count = binary.count('1')
            if count == k:
                ans += nums[i]
        return ans 