#Grouping with Parentheses

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
a=mo.group(1)
print('Group 1 :'+a)
b=mo.group(2)
print('Group 2 :'+b)
c=mo.group(0)
print('Group 3 :'+c)
