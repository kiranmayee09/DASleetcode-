class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        count = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                count += 1
                i += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    result += 1

                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    result += 1
                    i += 1

        return result + count * 2
