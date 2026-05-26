class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)   # rows
        n = len(matrix[0])  # cols

        row = [0] * m
        col = [0] * n

        # Step 1: Mark rows and cols that contain 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Step 2: Set matrix cell to 0
        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

        return matrix