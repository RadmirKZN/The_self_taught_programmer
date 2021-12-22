import re
string = 'Два даа.'
s = re.findall("д[ав]а",
                string,
                re.IGNORECASE)
print(s)