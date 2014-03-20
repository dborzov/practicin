import re

stronger = ' dsfdsf <a href="/wiki/Blood_Under_the_Skin" title="Blood Under the Skin">'

r = re.search('<a href="(.+)" title="(.+)">',stronger)

print r.group(2)