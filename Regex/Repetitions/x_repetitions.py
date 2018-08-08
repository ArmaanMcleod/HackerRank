import re

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
