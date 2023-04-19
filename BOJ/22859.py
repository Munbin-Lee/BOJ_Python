import re

input = open(0).read()
output = ''

for div in re.finditer('<div .*?</div>', input):
    div = div.group()
    title = re.search('title="(.*?)"', div).group(1)
    output += 'title : ' + title + '\n'
    for p in re.finditer('<p>(.*?)</p>', div):
        p = p.group(1)
        p = re.sub('<.*?>', '', p)
        p = re.sub('^ ', '', p)
        p = re.sub('$ ', '', p)
        p = re.sub(' {2,}', ' ', p)
        output += p + '\n'

print(output)
