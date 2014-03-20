import re


groomer = "<td> 1 </td>  <td>  2 </td>"
r = re.finditer('<td>.+</td>',groomer)

for each in r:
    print each.group()
    # fromer = each.start() 
    # ender = re.search('</td>',groomer[fromer:])
    # print 'AHA!'
    # print groomer[fromer:fromer+ender.end()]
