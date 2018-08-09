import re

Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
