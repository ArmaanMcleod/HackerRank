import re

test_string = input()

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	# Do not delete 'r'.

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
