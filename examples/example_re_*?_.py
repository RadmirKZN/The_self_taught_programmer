import re
t = "_один_ _два_ _три_"
found = re.findall("_.*?_", t)
for math in found:
    print(math)