class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            
        vowels = "aeiou"
        max_vowel = 0
        max_consonant = 0

        for ch in freq:
            if ch in vowels:
                max_vowel = max(max_vowel, freq[ch])
            else:
                max_consonant = max(max_consonant, freq[ch])

        return max_vowel + max_consonant
