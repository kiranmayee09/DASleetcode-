class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """ stack = []

        for op in operations:

            if op == "+":
                stack.append(stack[-1] + stack[-2])
            
            elif op == "D":
                stack.append(stack[-1] * 2)
            
            elif op == "C":
                stack.pop()
            
            else:
                stack.append(int(op))

        return sum(stack) 

        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                del record[-1]
            else:
                record.append(int(op))

        return sum(record) """

        record = []
        total = 0

        for op in operations:
            if op == "+":
                score = record[-1] + record[-2]
                record.append(score)
                total += score
            elif op == "D":
                score = record[-1] * 2
                record.append(score)
                total += score
            elif op == "C":
                total -= record[-1]
                record.pop()
            else:
                score = int(op)
                record.append(score)
                total += score
        return total