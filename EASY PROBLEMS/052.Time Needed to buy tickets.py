class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        from collections import deque

        q = deque()

        for i in range(len(tickets)):
            q.append(i)

        time = 0

        while tickets[k] > 0:
            person = q.popleft()

            tickets[person] -= 1
            time += 1

            if tickets[person] > 0:
                q.append(person)

        return time