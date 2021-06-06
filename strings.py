# single line
my_string = 'Hello World'
my_string = "Hello World"

# Multiple line
my_string = f'''
 Hi John
 
 Let's have a meeting in the afternoon 
 regarding python
 
 Best regards,
 Ron
'''

# concatenate variable into string

sender = 'Ron'
recipient = "John"

my_string = 'Hi ' + recipient
my_string = 'Hi ' + recipient + ' this is ' + sender
# f-string formatting
my_string = f'Hi {recipient}'
my_string = f"Hi {recipient}"

# multiple lines with f-string formating
my_string = f'''
 Hi {recipient}
 
 Let's have a meeting in the afternoon 
 regarding python
 
 Best regards,
 {sender}
'''

# escaping characters
my_string = 'Ron\'s House'
my_string = "Ron \"chefboyronron\" Seminiano"

# Getting pieces of character in the string
my_string = 'Say hello to the world of python.'

# my_string = my_string[2]  # return y in Say
# my_string = my_string[-6]  # return y in python
# my_string = my_string[4:-11]  # return hello to the world | spaces are included to the count

# string functions
my_string = 'hello world'

uppercase = my_string.upper()  # upper case all letters
lowercase = my_string.lower()  # lower case all letters
strip = my_string.strip('h')  # remove a character into string
letter_count = my_string.count('o')  # returns 2 | check the occurrence of the character
character_count = len(my_string)  # count number of characters
capitalized = my_string.capitalize()  # capitalized first letter
lowercase_capital_letters = uppercase.casefold()  # lower case all capital letters

special_char = "ñ Ñ"
html_hex = special_char.encode(encoding="ascii",errors="backslashreplace")  # HTML entity hexadecimal
remove_char = special_char.encode(encoding="ascii",errors="ignore")  # remove the special character
char_desc = special_char.encode(encoding="ascii",errors="namereplace")  # return description of the character
char_mark = special_char.encode(encoding="ascii",errors="replace")  # replace the character with question marc (?)
html_dec = special_char.encode(encoding="ascii",errors="xmlcharrefreplace")  # HTML entity decimal

replace = special_char.replace('ñ', 'n')

endsWith = my_string.endswith('d')  # check the string end character | return boolean
find = my_string.find('w', 1, 7)  # return occurrence | index else -1
find = 'Hello' in my_string  # fine the character in the string using in operator
# print(my_string[find])

print(replace)

