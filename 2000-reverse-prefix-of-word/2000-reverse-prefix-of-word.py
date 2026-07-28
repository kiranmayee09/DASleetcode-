class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """ if ch not in word:
            return word
        indexch = word.index(ch)

        return word[indexch::-1] + word[indexch+1::] """

        stack = []

        if ch not in word:
            return word
        
        index = word.index(ch)

        for i in range(index + 1):
            stack.append(word[i])

        ans = ""

        while stack:
            ans += stack.pop()

        ans += word[index + 1::]

        return ans
