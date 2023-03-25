import re
pattern = r"[A-Z][a-z][0-9]"

if re.match(pattern,"Da0nnsdDauuuio"):
    print("Matched")