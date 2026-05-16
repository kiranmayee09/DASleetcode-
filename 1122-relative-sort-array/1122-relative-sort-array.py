class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        for num in arr2:
            for x in arr1:
                if x == num:
                    result.append(x)

        remaining = []

        for x in arr1:

            if x not in arr2:
                remaining.append(x)

        n = len(remaining)

        for i in range(n):
            for j in range(n - i -1):
                if remaining[j] > remaining[j + 1]:
                    remaining[j], remaining[j+1] = remaining[j+1], remaining[j]
        
        result.extend(remaining)

        return result 