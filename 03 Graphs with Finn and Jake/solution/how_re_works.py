import re


groomer = '<a href="/wiki/Prisoners_of_love" title="Prisoners of love">'
r = re.search('<a href="(\w+)" title="([\w\s]+)">',groomer)

if r:
    print r.group(0)
    print r.group(1)