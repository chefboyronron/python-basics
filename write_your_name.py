# Write your name
# 1 = # | 0 = blank space

letters = [
    {
        0: [1, 1, 1, 1, 1, 1],
        1: [1, 1, 0, 0, 1, 1],
        2: [1, 1, 1, 1, 0, 0],
        3: [1, 1, 0, 0, 1, 1],
        4: [1, 1, 0, 0, 1, 1]
    },
    {
        0: [1, 1, 1, 1, 1, 1],
        1: [1, 1, 0, 0, 1, 1],
        2: [1, 1, 0, 0, 1, 1],
        3: [1, 1, 0, 0, 1, 1],
        4: [1, 1, 1, 1, 1, 1]
    },
    {
        0: [1, 1, 0, 0, 1, 1],
        1: [1, 1, 1, 0, 1, 1],
        2: [1, 1, 1, 1, 1, 1],
        3: [1, 1, 0, 1, 1, 1],
        4: [1, 1, 0, 0, 1, 1]
    }
]

counter = 0
while counter <= 4:
    line = ''
    for letter in letters:
        maps = letter[counter]
        for map in maps:
            if map == 1:
                line += '#'
            if map == 0:
                line += ' '
        line += '  '
    print(line)
    counter += 1
else:
    print(':)')