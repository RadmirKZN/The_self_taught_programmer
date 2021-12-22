import re
x = 'Красивое лучше, чем уродливое.'
matches = re.findall ("Красивое", x)
print(matches)
