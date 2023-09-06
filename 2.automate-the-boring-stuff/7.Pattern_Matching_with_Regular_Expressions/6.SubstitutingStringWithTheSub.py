# Regex cannot only find text patterns but can also substitute new text in place
# The sub() method for regex objects is passed two arguments
# 1st argument is a string to replace any matches
# 2nd argument is the string for the regular expression
import re

namesRegex = re.compile(r'Agent \w+')
res = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(res)


# You can use the matched text itself as part of the substitution.
# Here we remove the Agent word and censor only the name
# (\w) will be associated with \1
agentNamesRegex = re.compile(r'Agent (\w)\w*')
res = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
print(res)

agentNamesRegex = re.compile(r'Agent (\w)(\w)\w*')
res = agentNamesRegex.sub(r'\1\2****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
print(res)