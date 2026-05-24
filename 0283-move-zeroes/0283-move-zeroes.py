class Solution(object):
    def moveZeroes(self, nums):
        
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        zerors = len(nums) - len(temp)

        temp.extend([0] * zerors)

        for i in range(len(nums)):
            nums[i] = temp[i]
        return nums
