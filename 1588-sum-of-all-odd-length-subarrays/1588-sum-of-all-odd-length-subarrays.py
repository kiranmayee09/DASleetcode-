class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)

        for i in range(n):
            current_sum = 0

            for j in range(i, n):
                current_sum += arr[j]

                length = j - i + 1

                if length % 2 == 1:
                    ans += current_sum
        return ans