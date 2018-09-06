import re
ret = re.match('[1-9]?\d$\100','100')
print(ret.group())

