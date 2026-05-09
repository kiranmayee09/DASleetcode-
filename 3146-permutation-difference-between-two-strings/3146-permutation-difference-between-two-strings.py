class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        ans = 0
        for i in range(len(s)):
            pos = t.index(s[i])
            ans +=abs(i - pos)
        return ans