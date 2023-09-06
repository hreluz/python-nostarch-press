# Matching complicated text patterns might require long, convoluted regular expressions.
# You can mitigate this by telling re.compile() function to ignore whitespace and
# comments inside the regular expression string.

# This "verbose mode" can be enabled by passing the variable re.VERBOSE as
# the 2nd argument to re.compile()
import re

# phoneRegex = re.compile(r'((\d{3}|(\d{3}\)?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# it can be spread the regular expression over multiple lines with comments

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # area code
    (\s|-|\.)?                  # separator
    \d{3}                       # first 3digits
    (\s|-|\.)?                  # separator
    \d{4}                       # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?# extension    
)''', re.VERBOSE)