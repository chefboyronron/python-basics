# Exercise - create weight converter from kg to lbs or lbs to kg

def check_weight(weight):
    if weight.isnumeric():
        unit = input("(L)lb or (K)kg: ")
        unit = unit.lower()
        check_unit(unit, weight)
    else:
        weight = input("Please enter your weight: ")
        check_weight(weight)


def check_unit(unit, weight):
    if unit != 'l' and unit != 'k':
        unit = input('Unit only accepts (L)lb or (K)kg: ')
        unit = unit.lower()
        check_unit(unit, weight)
    else:
        if unit == 'l':
            mass = round(int(weight) * 0.453592, 2)
            print(f'You are {mass} kg.')
        else:
            mass = round(int(weight) * 2.20462, 2)
            print(f'Your are {mass} lbs.')

        is_finish = True
        start_conversion(is_finish)


def start_conversion(is_finish):
    if not is_finish:
        weight = input("Please enter your weight: ")
        check_weight(weight)
    else:
        repeat = input("Do you want to start again? Y or N ")
        repeat = repeat.upper()

        if repeat != 'Y' and repeat != 'N':
            print('Wrong selected value, ending conversion..')
            return True

        if repeat == 'Y':
            is_finish = False
            start_conversion(is_finish)
        else:
            return True


is_finish = False
start_conversion(is_finish)
