import re

Regex_Pattern = r'^[1-3][0-2][xs0][30Aa][xsu][\.,]$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
