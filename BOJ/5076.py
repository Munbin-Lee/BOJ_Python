import re


def isLegal(line):
    stack = []
    for tag in re.findall('<.*?>', line):
        both = re.fullmatch('<.*?/>', tag)
        if both:
            continue

        close = re.fullmatch('</(.*?)>', tag)
        if close:
            if not stack:
                return False
            if stack[-1] != close.group(1):
                return False
            stack.pop()
            continue

        openAttr = re.fullmatch('<(.*?) .*?>', tag)
        if openAttr:
            stack.append(openAttr.group(1))
            continue

        open = re.fullmatch('<(.*?)>', tag)
        stack.append(open.group(1))
    return len(stack) == 0


for line in open(0).read().splitlines():
    if line == '#':
        continue
    res = isLegal(line) and 'legal' or 'illegal'
    print(res)
