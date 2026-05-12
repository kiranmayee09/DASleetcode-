class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            string = str(num)
            for i in string:
                ans.append(int(i))
        return ans

