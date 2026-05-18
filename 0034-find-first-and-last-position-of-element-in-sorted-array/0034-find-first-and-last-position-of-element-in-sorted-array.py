class Solution:

    def lower_bound(self, nums, target):

        low = 0
        high = len(nums) - 1

        ans = len(nums)

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] >= target:

                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans

    def upper_bound(self, nums, target):

        low = 0
        high = len(nums) - 1

        ans = len(nums)

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] > target:

                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans

    def searchRange(self, nums, target):

        first = self.lower_bound(nums, target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = self.upper_bound(nums, target) - 1

        return [first, last]