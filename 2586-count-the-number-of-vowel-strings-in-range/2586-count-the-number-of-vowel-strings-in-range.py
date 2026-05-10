class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(left, right+1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                result += 1
        return result 