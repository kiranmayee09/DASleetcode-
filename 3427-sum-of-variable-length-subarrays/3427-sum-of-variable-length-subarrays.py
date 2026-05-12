class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        
        prefix = [0] + list(accumulate(nums))

        total = 0

        for i in range(len(nums)):

            start = max(0, i - nums[i])

            total += prefix[i + 1] - prefix[start]

        return total