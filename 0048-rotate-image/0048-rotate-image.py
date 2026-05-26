class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # create new rotated matrix
        rotated = [[0] * n for _ in range(n)]

        # put elements in rotated position
        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]

        # copy back to original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]