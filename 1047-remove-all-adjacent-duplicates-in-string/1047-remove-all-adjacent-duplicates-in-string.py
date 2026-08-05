class Solution:
    def removeDuplicates(self, s: str) -> str:
        """ stack = []

        for ch in s:

            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack) """

        ans = ""

        for i in s:
            if ans and ans[-1] == i:
                ans = ans[:-1]
            else:
                ans += i
        return ans