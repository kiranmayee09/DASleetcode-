class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        indexch = word.index(ch)

        return word[indexch::-1] + word[indexch+1::]
