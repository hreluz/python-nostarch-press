"""You have to find every phone and number and email address in a long web or document
Steps for analysis

1. Get the text off the clipboard
2. Find all phone numbers and email addresses in the text
3. Paste them onto the clipboard

The code will need to do the following

1. Use the pyperclip module to copy and paste strings
2. Create two regexs, one for matching phone numbers and the other for
    matching email addresses
3. Find all matches, not just the first match, of both regexes
4. Neatly format the matched strings into a single string to paste
5. Display some kind of message if no matches were found in the text"""

import pyperclip, re

# 1. Create a Regex for Phone Numbers

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code -> optional because of ? and 3digits with or without ()
    (\s|-|\.)?              # separator -> optional can be a space, hyphen - or period (.)
    (\d{3})                 # first 3 digits
    (\s|-|\.)?              # separator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5))? # extension -> optional X spaces followed by ext,x or ext. and 2-5digits
    
)''', re.VERBOSE) #re.VERBOSE allow to split in multiple lines the regex

# 2. Create a Regex for Email Addresses
