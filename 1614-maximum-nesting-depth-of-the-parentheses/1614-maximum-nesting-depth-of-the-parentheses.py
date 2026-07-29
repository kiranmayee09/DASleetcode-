class Solution:
    def maxDepth(self, s: str) -> int:
        """ depth = 0
        max_depth = 0

        for ch in s:
            if ch == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            elif ch == ")":
                depth -= 1
        return max_depth """

        stack = []
        max_depth = 0

        for ch in s:
            if ch == "(":
                stack.append(ch)
                max_depth = max(max_depth, len(stack))

            elif ch == ")":
                stack.pop()

        return max_depth