#match, search, findall

'''
import re
pattern = r"Colour"
if re.match(pattern,"Red is a colour"):
    print("Match")
else:
    print("Not Matched")
'''

'''
import re
pattern = r"colour"
if re.search(pattern,"Red is a colour"):
    print("Match")
else:
    print("Not Matched")
'''

import re
pattern = r"colour"
print(re.findall(pattern,"Red is a colour, I like red colour"))
