# imports json and re used in exercise
# import date, get current date
import json
import re
from datetime import date

# Variables
integer = 10
string = 'string'
boolean = True
flt = 2.5

print(type(integer))  # <class 'int'>
print(type(string))  # <class 'str'>
print(type(boolean))  # <class 'bool'>
print(type(flt))  # <class 'float'>

if type(integer) == str:
    print(True)
else:
    print(False)

print('-' * 50)

# Exercise #1 - Input a patient name and age and check if the patient has record.

# Create a patients object with name and age property
patients = [
    {
        'name': 'John Smith',
        'age': '20'
    },
    {
        'name': 'Ron Seminiano',
        'age': '30'
    }
]
# count the patient count
patient_count = len(patients)
i = 0

name = input('Enter Name: ')
birth_year = input('Birth Year: ')
current_date = date.today()
dynamic_age = str(int(current_date.year) - int(birth_year))

print('=' * 20)

print('Name: ' + name)
print('Age: ' + dynamic_age)

# This also works, finding property using while loop
# pros: can return all properties value
# while i < patient_count:
#     if (name == patients[i]['name']) & (age == patients[i]['age']):
#         print('Type: Old patient')
#         break
#     i += 1
# else:
#     print('Type: New patient')

# Find property using regex key:value pair
# cons - you can't return the other properties value and has issue in separate search
find_string = '"name": "' + name + '", "age": "' + dynamic_age + '"'
# output: <re.Match object; span=(39, 62), match='"name": "Ron Seminiano"'>
patient_match = re.search(find_string, json.dumps(patients), re.M)

if patient_match == None:
    print('Type: New patient')
else:
    print('Type: Old patient')

print('=' * 20)
