import re
given=input()
pattern=r'([a-zA-Z0-9])\1+'
search=re.search(pattern,given)
print(search.group(0)[0]) if search else print(-1)
