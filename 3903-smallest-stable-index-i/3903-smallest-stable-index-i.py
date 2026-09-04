class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            maxvalue = minvalue = nums[i]
            for j in range(i):
                maxvalue = max(maxvalue, nums[j])
            for j in range(i + 1, n):
                minvalue = min(minvalue, nums[j])
            if maxvalue - minvalue <= k:
                return i
        return -1