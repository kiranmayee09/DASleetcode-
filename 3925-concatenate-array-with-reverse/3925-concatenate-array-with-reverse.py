class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        """ return nums + nums[::-1] """

        ans = []

        for x in nums:
            ans.append(x)
        
        for i in range(len(nums) -1, -1, -1):
            ans.append(nums[i])
        
        return ans