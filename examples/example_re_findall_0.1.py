import re
x = 'Красивое лучше, чем уродливое.'
matches = re.findall("красивое", x, re.IGNORECASE)
print(matches)