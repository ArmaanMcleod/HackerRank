import re

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
