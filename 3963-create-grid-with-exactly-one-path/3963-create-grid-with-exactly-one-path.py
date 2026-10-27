class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = [""] * m

        grid[0] = "." * n

        row = "#" * (n - 1) + "."

        for i in range(1, m):
            grid[i] = row

        return grid
