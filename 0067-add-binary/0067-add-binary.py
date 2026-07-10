class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to decimal integers
        """ num1 = int(a, 2)
        num2 = int(b, 2)

        # Add them
        total = num1 + num2

        # Convert decimal back to binary
        return bin(total)[2:]"""

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:

            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1

            ans.append(str(total % 2))
            carry = total // 2

        return "".join(ans[::-1])
