#finding vowels 

import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
find = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(find)
