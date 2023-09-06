"""
Shorthand
character class     Represents

    \d              Any numeric digit from 0 to 9
    \D              Any character that is not a numeric digit from 0 to 9
    \w              Any letter, numeric, digit or the underscore character
                    (Think of this as matching "word" characters)
    \W              Any character that is not a letter, numeric digit,
                    or the underscore character
    \s              Any space, tab, or newline character (Think of this as
                    matching "space" characters)
    \S              Any character that is not a space, tab, or newline

"""

import re

# \d+\s\w+ will match a text that has one or more numeric digits (\d+)
# followed by one or more letter /digit/
xmasRegex = re.compile(r'\d+\s\w+')
res = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(res)

print('\n----------Making your own character classes----------')
# You can define your own character class using square brackets
# For example, the character class [aeiouAEIOU] will match any vowel, both
# lowercase and uppercase

vowelRegex = re.compile(r'[aeiouAEIOU]')
res = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(res)

# You can also include ranges of letters or numbers by using hyphen
# For example, the character class [a-zA-Z0-9] will match all lowercase
# letters, uppercase letters and numbers

# NOTE: inside the square brackets, the normal regular expression symbols are not interpreted
# as such and there is no need to escape .,*,? or () characters with a preceding backslash
# [0-5.] will match digits 0 to 5 and a period

# By placing a caret char (^) just after class' opening bracket, you can make a negative class

vowelRegex = re.compile(r'[^aeiouAEIOU]')
res = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(res)

print('\n----------The Caret and Dollar Sign characters----------')
# You can also use the carey symbol (^) at the start of a regex to indicate that
# a match must occur at the beginning of the searched text
# And, you can put a dollar sign ($) at the end of the regex to indicate the string
# must end with this regex pattern
# And you can use the ^ and $ together to indicate that entire must match the regex

beginsWithHello = re.compile(r'^Hello')
res = beginsWithHello.search('Hello World!')
print(res)
res = beginsWithHello.search('He said Hello.')
print(res is None)

print('\n---------- r\d$ regular expression ----------')
# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9\
endsWithNumber = re.compile(r'\d$')
res = endsWithNumber.search('Your number is 42')
print(res)
res = endsWithNumber.search('Your number is 42 yeah')
print(res is None)

print('\n---------- r^\d+$ regular expression ----------')
# The r'^\d+$' regular expression string matches strings that both begin and end with one or more
# numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
res = wholeStringIsNum.search('1234567890')
print(res)
res = wholeStringIsNum.search('12 4535456')
print(res is None)

print('\n---------- The Wildcard character ----------')
# The . (or dot) in a regular expression is called a wildcard and will match any character

atRegex = re.compile(r'.at')
res = atRegex.findall('The cat in the hat sat on the flat mat')
print(res)


print('\n---------- Matching Everything with Dot-Star ----------')
# You can use the dot-star (.*) to stand in for that "anything"

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.groups())

# It will always try to match as much text as possible.
# To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?)
text = '<To serve man> for dinner.>'
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search(text)
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search(text)
print(mo.group())

print('\n---------- Matching Newlines with the Dot Character ----------')
# The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to
# re.compile(), you can make the dot character match all characters, including the newline character
text = 'Serve the public trust.\nProtect the innocent.\nUphold the law'
noNewlineRegex = re.compile('.*')
res = noNewlineRegex.search(text)
print(res.group())

newLineRegex = re.compile('.*', re.DOTALL)
res = newLineRegex.search(text)
print(res.group())