class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        operations = 0

        for num in nums:
            operations += maximum - num

        return operations