# Exercise - Car simulator
# start, stop, forward, backward, left, right, quit

commands = ['start', 'quit']
move_commands = ['forward', 'backward', 'left', 'right', 'stop']
is_started = False
engine_on = False
is_stop = False
i = 0
failed_count = 0
while i < 1:
    i += 1
    command = input("Command: ").lower()

    if command in commands or command in move_commands:

        if command in move_commands and not is_started:
            print('Please start the car.')

        if command == 'start' and is_started:
            print('Engine already started.')

        if command == 'start' and not is_started:
            print('Engine Start.')
            engine_on = True
            is_started = True

        if command == 'forward' and is_started:
            print('Car moving forward.')
            is_stop = False

        if command == 'backward' and is_started:
            print('Car moving backward')
            is_stop = False

        if command == 'left' and is_started:
            print('Car turning left.')
            is_stop = False

        if command == 'stop' and is_started:
            print('Car stopped.')
            is_stop = True

        if command == 'right' and is_started:
            print('Car turning right.')
            is_stop = False

        if command == 'quit' and not is_stop:
            print('please stop the car.')

        if command == 'quit' and is_stop:
            print('Engine off')
            engine_on = False
            break

    else:
        if failed_count < 2:
            print('Unknown command.')
        else:
            print('Car is crashed.')
            break

        failed_count += 1

    i = 0
else:
    print('Car is broken, go to the mechanics :)')
