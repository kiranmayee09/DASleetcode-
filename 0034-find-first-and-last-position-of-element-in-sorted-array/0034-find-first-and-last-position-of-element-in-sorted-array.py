class Solution:
    def searchRange(self, nums, target):
        first = self.first_occ(nums, target)

        if first == -1:
            return [-1, -1]

        last = self.last_occ(nums, target)

        return [first, last]

    def first_occ(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ans = mid
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def last_occ(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1 

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ans = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans 