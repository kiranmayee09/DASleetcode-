class Solution(object):
    def moveZeroes(self, nums):
        
        temp = [0] * len(nums)
        index = 0
        for num in nums:
            if num != 0:
                temp[index] = num
                index += 1
                
        for i in range(len(nums)):
            nums[i] = temp[i]
        
        return nums
