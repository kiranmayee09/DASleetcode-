import math
class Solution:
    def SumByD(self, nums, div):
        return sum(math.ceil(x / div) for x in nums)

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) > threshold:
            return -1

        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.SumByD(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low

