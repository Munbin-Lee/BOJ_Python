import sys
input = sys.stdin.readline


def getDiff(a, b):
    cnt = 0
    for k, v in enumerate(a):
        if (v != b[k]):
            cnt += 1
    return cnt


def dfs(word, cnt):
    global words, mnCnt, visited

    if word == target:
        if mnCnt == 0 or cnt < mnCnt:
            mnCnt = cnt

    visited.append(word)
    for newWord in words:
        if getDiff(word, newWord) == 1 and newWord not in visited:
            dfs(newWord, cnt+1)


def solution(b, t, w):
    global begin, target, words, visited, mnCnt

    begin = b
    target = t
    words = w
    visited = []
    mnCnt = 0
    dfs(begin, 0)
    return mnCnt


# vscode용
_begin = "hit"
_target = "dot"
_words = ["hot", "dot", "dog", "lot", "log", "cog"]
res = solution(_begin, _target, _words)
print(mnCnt)
