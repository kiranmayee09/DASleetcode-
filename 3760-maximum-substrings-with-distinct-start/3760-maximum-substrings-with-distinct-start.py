class Solution:
    def maxDistinct(self, s: str) -> int:
        """ return len(set(s)) """

        seen = set()

        for ch in s:
            seen.add(ch)
        
        return len(seen)