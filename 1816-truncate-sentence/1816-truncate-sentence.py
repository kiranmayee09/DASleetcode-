class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        words[:k]
        return " ".join(words[:k])