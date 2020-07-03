# wildcard character 

import re
atRegex = re.compile(r'.at')
card = atRegex.findall('The cat in the hat sat on the flat mat.')
print(card)
