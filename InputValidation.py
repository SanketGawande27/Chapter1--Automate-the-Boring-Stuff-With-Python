#Regex 

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 123-890-1212.')
print('Phone Number Found: '+mo.group())

 

