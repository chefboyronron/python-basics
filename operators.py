# logical operators
# and | or | not
accredited = True
in_manila = False

if accredited and in_manila:
    print('Proceed')

if accredited or in_manila:
    print('Proceed')

if accredited and not in_manila:
    print('Not accessible')

# Comparison operators
# == | != | > | < | >= | <=

x = 1
y = 2

if x == y:
    print('x is equal to y')

if x != y:
    print('x is not equal to y')

if x > y:
    print('x is greater than y')

if x < y:
    print('x is less than y')

if x >= y:
    print('x is gt or equal to y')

if x <= y:
    print('x is lt or equal to y')

# for more list of operators visit
# https://www.w3schools.com/python/python_operators.asp