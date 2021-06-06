# Exercise - create weight converter from kg to lbs or lbs to kg

# import regex module
import re


def check_unit(unit, weight):
    # check if user input is [lLkK] else re enter the unit
    if unit != 'l' and unit != 'k':
        unit = input('Unit only accepts (L)lb or (K)kg: ').lower()
        check_unit(unit, weight)
    else:
        # compute the weight based on the user input
        if unit == 'l':
            mass = round(weight * 0.45359237, 1)
            print(f'You are {mass} kg.')
        else:
            mass = round(weight * 2.205, 1)
            print(f'Your are {mass} lbs.')

        # after printing computation ask if the user want to convert again.
        start_conversion(True)


def start_conversion(finish):
    # Check if the user want to end the conversion | default false
    if not finish:
        weight = input("Please enter your weight: ")
        # check if the user input for weight is float or int else re enter the weight
        if re.match('^[0-9.]*$', weight):
            weight = float(weight)
            unit = input("(L)lb or (K)kg: ").lower()
            check_unit(unit, weight)
        else:
            start_conversion(False)
    else:
        repeat = input("Do you want to start again? Y or N ")
        repeat = repeat.upper()

        # if the user not selected either [yYnN] end the conversion
        if repeat != 'Y' and repeat != 'N':
            print('Wrong selected value, ending conversion..')
            return True

        # if the user want to convert again
        if repeat == 'Y':
            start_conversion(False)
        else:
            # end the conversion
            return True


is_finish = False
# Execute conversion
start_conversion(is_finish)
