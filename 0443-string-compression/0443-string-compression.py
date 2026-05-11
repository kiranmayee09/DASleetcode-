class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        n = len(chars)

        while i < n:
            char = chars[i]
            count = 1
            while i + 1 < n and chars[i] == chars[i+1]:
                count += 1
                i += 1
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            i += 1
    
        return write