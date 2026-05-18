class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        frist = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if frist == -1:
                    frist = i
                last = i
        return [frist, last]