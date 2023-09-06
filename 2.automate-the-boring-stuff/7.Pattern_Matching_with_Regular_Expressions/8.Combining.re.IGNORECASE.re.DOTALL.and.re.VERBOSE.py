# What if you want to use re.VERBOSE to write comments in your regular expression
# but also want to use re.IGNORECASE to ignore capitalization?
import re

someRegexValue =  re.compile('foo', re.IGNORECASE | re.DOTALL)

# Including all 3 options in the 2nd argument
someRegexValue2 =  re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
