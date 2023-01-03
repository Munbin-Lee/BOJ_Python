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

    for k, newWord in enumerate(words):
        if getDiff(word, newWord) == 1 and not visited[k]:
            visited[k] = True
            dfs(newWord, cnt+1)
            visited[k] = False


def solution(b, t, w):
    global begin, target, words, mnCnt, visited

    begin = b
    target = t
    words = w
    visited = [False for i in range(len(words))]
    mnCnt = 0
    dfs(begin, 0)
    return mnCnt


# vscode용
_begin = "dog"
_target = "cog"
_words = ["hot", "dot", "dog", "lot", "log", "cog"]
res = solution(_begin, _target, _words)
print(mnCnt)
