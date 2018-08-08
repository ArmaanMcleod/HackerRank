import re

Regex_Pattern = r'^[^0-9][^aeiou][^bcDF][^\s][^AEIOU][^\.\,]$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
