from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        studentQueue = deque(students)
        sandwichesStack = sandwiches[::-1]

        sandwichMissed = 0

        while studentQueue:
            if sandwichesStack[-1] == studentQueue[0]:
                sandwichesStack.pop()
                studentQueue.popleft()
                sandwichMissed = 0
            else:
                studentQueue.append(studentQueue.popleft())
                sandwichMissed += 1

                if sandwichMissed == len(studentQueue):
                    break

        return len(studentQueue)










        """ count0 = students.count(0)
        count1 = students.count(1)

        for s in sandwiches:
            if s == 0:
                if count0 == 0:
                    return count1
                count0 -= 1
            else:
                if count1 == 0:
                    return count0
                count1 -= 1
        return 0 """

        