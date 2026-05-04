class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_vals = []
        for p in points:
            x_vals.append(p[0])

        x_vals.sort()

        max_width = 0
        for i in range(1, len(x_vals)):
            gap = x_vals[i] - x_vals[i - 1]
            max_width = max(max_width, gap)

        return max_width