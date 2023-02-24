import re

print([x for line in open('mbox.txt') for x in re.findall('^From: ([a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+)', line)])
