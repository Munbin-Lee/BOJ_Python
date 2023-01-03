from collections import deque
import sys
input = sys.stdin.readline


def solution(tickets):
    tickets.sort()
    dq = deque()
    dq.append(("ICN", ["ICN"], tickets))
    while dq:
        airport, trace, _tickets = dq[0]
        dq.popleft()

        if not len(_tickets):
            return trace

        for k, ticket in enumerate(_tickets):
            if ticket[0] == airport:
                dq.append((ticket[1], trace + [ticket[1]],
                          _tickets[:k]+_tickets[k+1:]))


# vscode용
t = [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]
ans = solution(t)
print(ans)
