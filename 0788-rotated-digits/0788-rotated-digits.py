class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n+1):
            valid = True
            changed = False

            temp = num

            while temp > 0:
                digit = temp % 10

                if digit in[3, 4, 7]:
                    valid = False
                    break
                if digit in [2, 5, 6, 9]:
                    changed = True

                temp //= 10

            if valid and changed:
                count += 1
        return count
