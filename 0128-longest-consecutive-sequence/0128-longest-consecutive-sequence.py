class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num
                curr_longest = 1
                while curr + 1 in nums_set:
                    curr += 1
                    curr_longest += 1
                longest = max(longest, curr_longest)
        return longest
             