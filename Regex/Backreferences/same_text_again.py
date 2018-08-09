import re

Regex_Pattern = r'^([a-z])(\w)(\s)([^\w])(\d)([^\d])([A-Z])([a-zA-Z])([aeiouAEIOU])([^\s])\1\2\3\4\5\6\7\8\9\10$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
