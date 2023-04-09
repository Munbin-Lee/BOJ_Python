import re


def isValid(line):
    context = []

    # 인코딩
    line = line.replace('&lt;', '')
    line = line.replace('&gt;', '')
    line = line.replace('&amp;', '')

    # &xHEX; HEX는 양의 짝수 자릿수의 16진수여야 하며, 0~9 또는 알파벳 A~F 대소문자로 이루어진다.
    for i in re.finditer('&', line):
        num = re.search('^&x([0-9a-fA-F]+);', line[i.start():])
        if not num or len(num.group(1)) % 2 == 1:
            return False

    # 태그는 숫자 또는 알파벳 소문자로 이루어진 문자열이어야 한다.
    for i in re.finditer('<', line):
        empty = re.search('^<[0-9a-z]+/>', line[i.start():])
        opn = re.search('^<([0-9a-z]+)>', line[i.start():])
        clse = re.search('^</([0-9a-z]+)>', line[i.start():])
        if not (empty or opn or clse):
            return False
        if opn:
            context.append(opn.group(1))
        elif clse:
            if not context or context[-1] != clse.group(1):
                return False
            context.pop()

    # 평문에 >는 포함되면 안 된다.
    for i in re.finditer('>', line):
        valid = re.search('<[0-9a-z/]+$', line[:i.start()])
        if not valid:
            return False

    # 문서 전체가 파싱된 후에는 context 스택은 비어 있어야 한다.
    if context:
        return False

    return True


for line in open(0).readlines():
    res = isValid(line) and "valid" or "invalid"
    print(res)
