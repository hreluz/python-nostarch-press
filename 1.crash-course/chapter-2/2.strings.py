name = "hector lavoe"
print(name.title())

name = "hECTOR lAVOE"
print(name.title())

name = "it was lowercase"
print(name.upper())

name = "IT WAS UPPERCASE"
print(name.lower())


# Using Variables in Strings
print("##### Using Variables in Strings #####")

# F FORMAT 3.6 >
# Display variables inside a string
first_name = "ruben"
last_name = "blades"
full_name = f"{first_name} {last_name}"
print(full_name)


message = f"Hello {full_name.title()}"
print(message)

# F FORMAT 3.6 <

first_name = "ruben"
last_name = "blades"
full_name = "Hello {} {}".format(first_name,last_name)
print(full_name)

# Adding Whitespace to Strings with Tabs or Newlines
print("No Tab")
print("\tWith Tab")

print("Languages:\nPython\nC\nJavascript")

# Stripping Whitespace
print("##### Stripping Whitespace #####")
favourite_language = "Python "
print(len(favourite_language), favourite_language)
print(len(favourite_language.rstrip()), favourite_language)
favourite_language = " Javascript"
print(len(favourite_language), favourite_language)
print(len(favourite_language.lstrip()), favourite_language)
favourite_language = "  Android "
print(len(favourite_language), favourite_language)
print(len(favourite_language.lstrip()), favourite_language)

# Avoiding Syntax Errors with Strings
print("##### Avoiding Syntax Errors with Strings #####")
# message = 'One of Python's strengths is its diverse community.'
# print(message)

print("#### Exercises ####")
name = "Hector Lavoe"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)
message = message.lower()
print(message)
message = message.upper()
print(message)
message = message.title()
print(message)
famous_person = "Albert Einstein "
quote = f'{famous_person.rstrip()} once said, "A person who never made a\nmistake never tried anything new.'
print(quote)