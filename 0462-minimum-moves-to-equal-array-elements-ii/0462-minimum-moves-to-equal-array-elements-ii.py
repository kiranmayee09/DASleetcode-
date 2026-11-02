class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        k = n // 2

        left = 0
        right = n - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            i = left
            j = right

            while i <= j:
                while nums[i] < pivot:
                    i += 1
                
                while nums[j] > pivot:
                    j -= 1

                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if k <= j:
                right = j
            elif k >= i:
                left = i
            else:
                median = nums[k]
                break

        moves = 0

        for x in nums:
            moves += abs(x - median)

        return moves