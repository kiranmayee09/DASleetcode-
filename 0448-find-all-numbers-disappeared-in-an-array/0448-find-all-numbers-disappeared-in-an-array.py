class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in range(len(nums)):
            arr[nums[i] - 1] = -1

        result = []
        for j in range(len(arr)):
            if arr[j] == 0:
                result.append(j + 1)
                
        return result