import re

s = 'abc'
re = re.sub('([a-z])', 'a\\1', s)
print(re)
