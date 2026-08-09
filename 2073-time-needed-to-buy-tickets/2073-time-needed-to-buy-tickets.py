class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """ res = 0

        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)

        return res """

        q = deque(range(len(tickets)))
        time = 0

        while q:
            person = q.popleft()

            tickets[person] -= 1
            time += 1

            if person == k and tickets[person] == 0:
                return time

            if tickets[person] > 0:
                q.append(person)