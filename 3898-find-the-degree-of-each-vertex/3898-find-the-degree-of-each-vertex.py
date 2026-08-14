class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        ans = [0] * n

        for i in range(n):
            ans[i] = matrix[i].count(1)
        
        return ans