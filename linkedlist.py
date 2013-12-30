# Kirk Boyer
# Sunday, Dec. 29

# This challenge is a sequence of sites with url
# www.pythonchallenge.com/pc/def/linkedlist.php?nothing=#####
# where the last part is a 5-digit number. 

# My guess is that eventually they'll stop the pattern at some point and either
# give another hint about the next challenge's url, or give it directly.
# Either way, there are only so many 5-digit numbers.

import urllib.request
import re

# original starting point: nothing = "12345"
nothing = "25357"
theUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

site = urllib.request.urlopen(theUrl+nothing)
pattern = re.compile("the next nothing is ([0-9]+)")
result = pattern.findall(site.read().decode())

while result != []:
    print("nothing is now: ")
    print(nothing)
    nothing = result[0]
    site = urllib.request.urlopen(theUrl+nothing)
    result = pattern.findall(site.read().decode())

 print(nothing)
