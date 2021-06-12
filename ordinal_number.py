# experimental playgrounds
# power of the number. eq squared, cube etc.
import re

result = []
number = 1
power = 4
iteration = 5
ordinal = 'th'
while number <= iteration:
    factorial = number ** power
    result.append(number ** power)
    if re.match('[123]*$', str(power)):
        if re.match('[1]*$', str(power)):
            ordinal = 'st'
        if re.match('[2]*$', str(power)):
            ordinal = 'nd'
        if re.match('[3]*$', str(power)):
            ordinal = 'rd'
    message = f'{number} to the {power}{ordinal} power is {factorial}'
    print(message)
    number += 1
else:
    print(result)
