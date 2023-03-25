'''
import re
pattern = r"^colo.r$"

if re.match(pattern,"colour"):
    print("Matched")


import re
pattern = r"ab*"

if re.match(pattern,"aaacolour"):
    print("Matched")


import re
pattern = r"a+"

if re.match(pattern,"aaacolour"):
    print("Matched")


import re
pattern = r"ice(-)?cream"

if re.match(pattern,"icecream"):
    print("Matched")
'''

import re
pattern = r"a{1,3}$"

if re.match(pattern,"aaaa"):
    print("Matched")
