class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        for i in range(len(order)):
            if order[i] in friends:
                result.append(order[i])
        return result 
