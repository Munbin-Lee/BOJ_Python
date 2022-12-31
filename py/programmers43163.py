from collections import deque
import sys
input = sys.stdin.readline


def getDiff(a, b):
    cnt = 0
    for k, v in enumerate(a):
        if (v != b[k]):
            cnt += 1
    return cnt


def solution(begin, target, words):
    visited = [False for i in range(len(words))]
    dq = deque()
    dq.append((begin, 0))
    while dq:
        tp = dq[0]
        dq.popleft()
        word = tp[0]
        dist = tp[1]
        if word == target:
            return dist
        for k, newWord in enumerate(words):
            if getDiff(word, newWord) == 1 and not visited[k]:
                visited[k] = True
                dq.append((newWord, dist+1))
    return 0


# vscode용
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
res = solution(begin, target, words)
print(res)
