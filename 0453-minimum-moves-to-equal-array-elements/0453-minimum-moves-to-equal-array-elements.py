class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minelement = min(nums)
        operations = 0

        for i in range(len(nums)):
            operations += nums[i] - minelement

        return operations