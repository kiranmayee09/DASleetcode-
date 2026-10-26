class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_map = "0123456789abcdef"
        result = []

        num &= 0xFFFFFFFF

        while num:
            result.append(hex_map[num & 0XF])
            num >>= 4

        return "".join(reversed(result))