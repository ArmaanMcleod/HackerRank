import re

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
