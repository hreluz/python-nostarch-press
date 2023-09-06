# Normally, regular expressions match text with the exact casing you specify
# The following regexes match completely different strings
import re

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('rob0cop')
regex4 = re.compile('Roboc0p')

# But for without worrying whether they're uppercase or lowercase

robocop = re.compile(r'robocop', re.I)
res = robocop.search('RoboCop is part man, part machine, all cop')
print(res.group())

res = robocop.search('ROBOCOP protects the innocent')
print(res.group())

res = robocop.search('Al, why does your programming book talk about robocop so much?')
print(res.group())