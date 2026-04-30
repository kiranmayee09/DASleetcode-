class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for i in range(len(encoded)):
            next_val  = encoded[i] ^ arr[i]
            arr.append(next_val)
        return arr
        