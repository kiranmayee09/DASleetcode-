class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = self.merge_sort(nums)
        n = len(nums)
        return res[n - k]

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result