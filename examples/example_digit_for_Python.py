import re
line = "123?34 ghbdtn?"
m = re.findall("\d",
               line,
               re.IGNORECASE)
print(m)