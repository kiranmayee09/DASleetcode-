class Solution:
    def minLength(self, s: str) -> int:

        """ stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= 2:
                if stack[-2] == "A" and stack[-1] == "B":
                    stack.pop()
                    stack.pop()
                
                elif stack[-2] == "C" and stack[-1] == "D":
                    stack.pop()
                    stack.pop()
        return len(stack) 

        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B") or
                (stack[-2] == "C" and stack[-1] == "D")
            ):
                stack.pop()
                stack.pop()
        return len(stack) """

        stack = []

        for ch in s:

            if stack:
                if (stack[-1] == "A" and ch == "B") or (stack[-1] == "C" and ch == "D"):
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return len(stack)
        
