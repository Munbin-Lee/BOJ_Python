import re
import copy

ls = []


def findUsers(users, ban):
    res = []
    pat = ban.replace('*', '.')
    for user in users:
        matched = re.fullmatch(pat, user)
        if matched:
            res.append(matched.group())
    return res


def dfs(idx, visited, bans, dict):
    global list

    if idx == len(bans):
        ls.append(visited)
        return
    ban = bans[idx]
    for matched in dict[ban]:
        if matched in visited:
            continue

        visited.add(matched)
        dfs(idx + 1, copy.deepcopy(visited), bans, dict)
        visited.remove(matched)


def solution(users, bans):
    global ls

    dict = {}
    for ban in bans:
        dict[ban] = findUsers(users, ban)
    dfs(0, set(), bans, dict)

    ls2 = []
    for l in ls:
        ls2.append(sorted(l))
    st = set(map(tuple, ls2))
    print(st)
    return len(st)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]))
