class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            for j in range(1, n):
                index = (i+j) % n
                if nums[index] > nums[i]:
                    ans[i] = nums[index]
                    break
        return ans