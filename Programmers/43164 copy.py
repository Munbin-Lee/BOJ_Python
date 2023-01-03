from collections import deque
import sys
input = sys.stdin.readline


def solution(tickets):
    tickets.sort()
    answer = []
    temp = "ICN"
    i = len(tickets)
    answer.append(temp)
    tempList = []
    for j in range(i):
        for T1 in tickets:
            if T1[0] == temp:
                tempList.append(T1)
        tempList.sort()
        temp = tempList[0][1]
        answer.append(temp)
        tickets.remove(tempList[0])
        tempList = []
    return answer


# vscode용
t = [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]
ans = solution(t)
print(ans)
