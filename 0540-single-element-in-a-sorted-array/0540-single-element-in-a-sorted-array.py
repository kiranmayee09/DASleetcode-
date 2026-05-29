class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)

        ans = 0
        for i in range(n):
            ans ^= nums[i]
        return ans 