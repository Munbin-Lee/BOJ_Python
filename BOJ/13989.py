import re

capPat = r"\b[A-Z][a-z]+\b"
abbrPat = re.compile("({} )+{}".format(capPat, capPat))

for line in open(0).read().split('\n'):
    idx = 0
    for abbr in abbrPat.finditer(line):
        ln = abbr.span()[0]
        print(line[idx:ln], end='')
        idx = abbr.span()[1]
        ls = [" ("]
        for word in abbr.group().split():
            ls.append(word)
            ls.append(' ')
            print(word[0], end='')
        ls.pop()
        ls.append(')')
        print(''.join(ls), end='')
    print(line[idx:], end='')
    print()
