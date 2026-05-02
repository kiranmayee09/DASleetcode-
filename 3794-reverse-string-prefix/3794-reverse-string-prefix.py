class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        frist = s[:k]
        rev = frist[::-1]
        rest = s[k:]
        return rev + rest