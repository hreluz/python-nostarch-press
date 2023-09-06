import re

text = 'My number is 415-555-4242'

# Matching Regex Objects
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(text)
print('Phone number found: ' + mo.group())


print('----------Grouping with Parentheses----------')
# To separate the area code from the rest of the phone number
# Adding parentheses will create groups in the regex/

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(text)
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# To retrieve all groups at once, use the groups methods
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print('----------Grouping Parentheses with Parentheses ----------')
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))

# Special characters to scape
# . ^ $ * + ? { } [ ] \ | ( )
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)


print('\n----------Matching multiple Groups with the Pipe ----------')
# This will match either Batman or Tina Fey
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

print('\n')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.groups())

print('\n----------Optional Matching with the Question Mark----------')
# The ? part of the regular expression means that the patter is an optional group
batRegex = re.compile(R'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group(), mo1.group(1))

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group(), mo2.group(1))

print('\n')
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search(text)
print(mo1.group())

mo2 = phoneNumRegex.search('My number is 555-4242')
print(mo2.group())

print('\n----------Matching Zero or More with the Star ----------')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batwowowoman')
print(mo3.group())

print('\n----------Matching One or More with the Plus ----------')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwowowoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batman')
print(mo3)

print('\n----------Matching Specific Repetitions with Braces ----------')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2)

# Regex will return the possible maximum by default
haRegex = re.compile(r'(Ha){3,5}')
mo3 = haRegex.search('HaHaHaHaHaHaHaHa')
print(mo3.group())


# This regex will return the possible shortes
haRegex = re.compile(r'(Ha){3,5}?')
mo4 = haRegex.search('HaHaHaHaHaHaHaHa')
print(mo4.group())


print('\n----------The findall method ----------')
# search will return a Match object of the first matched text in the searched string
# the findall method will return the strings of every match in the searched string

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
text2 = 'Cell: 415-555-9999 Work: 212-555-0000'

print('The search method:')
mo = phoneNumRegex.search(text2)
print(mo.group())

print('The findall method with no groups:')
print(phoneNumRegex.findall(text2))

print('The findall method with groups:')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall(text2))
