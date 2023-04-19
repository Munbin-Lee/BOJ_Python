n = int(input())
r = ''
t = ' '*4
o = '{'
c = '}'
if n == 0:
    r += 'BOJ 20000'
if n == 1:
    r += f'#include <cstdio>\nint main(){o}\n{t}int N;\n{t}scanf("%d",&N);\n   '
    for i in range(1, 20001):
        r += f' if(N=={i}){o}\n{t*2}puts("'+f'{4*i}");\n{t}{c}\n{t}else'
    r += f'{o}\n{t*2}puts("Still working on it...");\n{t}{c}\n{t}return 0;\n{c}'
if n == 2:
    l = ['!', 'geg', 'udu', 'eJe', 'ini',
         'nln', 'nOn', 'ooo', 'kjk', 'aea', 'B']
    for i in l:
        t = i
        for c in r:
            t += c+i
        r = t
print(r)
