class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                small = words[i]
                big = words[j]

                if big.startswith(small) and big.endswith(small):
                    count += 1
        return count
        