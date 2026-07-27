class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """ ans = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    ans.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans.append(ch)
        
        return "".join(ans) """

        stack = []
        ans = []

        for ch in s:

            if ch == '(':
                if stack:
                    ans.append(ch)
                stack.append(ch)

            else:
                stack.pop()

                if stack:
                    ans.append(ch)
                    
        return "".join(ans)