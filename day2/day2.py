# Description: Day 2

def read_input_string(textfile):
    with open(textfile) as f:
        input_data = [line.strip() for line in f]
    return input_data

# modified code from GPT
def is_game_possible(input_str):
    cube_counts = {"red": 12, "green": 13, "blue": 14}

    # remove the Game XX: from input_str
    input_str = input_str[input_str.find(':')+2:]

    print('input_str: ' + input_str)

    for round in input_str.split(";"):
        print('round: ' + round)
        selections = round.split(",")
        print(selections)

        for selection in selections:
            print(selection)
            count, colour = selection.strip().split()
            count = int(count)
            print(count)
            print(colour)
            colour = colour.lower()

            if count < 0 or count > cube_counts[colour]:
                print('its false')
                return False  # negative or excessive cube count

    return all(count >= 0 for count in cube_counts.values())

def fewest_cube_config(input_str):
    cube_counts = {"red": 0, "green": 0, "blue": 0}

    # remove the Game XX: from input_str
    input_str = input_str[input_str.find(':')+2:]

    print('input_str: ' + input_str)

    for round in input_str.split(";"):
        print('round: ' + round)
        selections = round.split(",")
        print(selections)

        for selection in selections:
            print(selection)
            count, colour = selection.strip().split()
            count = int(count)
            print(count)
            print(colour)
            colour = colour.lower()

            if count > cube_counts[colour]:
                cube_counts[colour] = count
    
    power = cube_counts['red'] * cube_counts['green'] * cube_counts['blue']

    return power

def solve_day2_part1(input_data):
    data = read_input_string(input_data)

    result_part1 = 0

    counter = 1

    for line in data:
        # game ID always increments by 1
        # we will just use a counter
        gameID = counter
        if is_game_possible(line) == True:
            print('CURRENT RESULT ' + str(result_part1))
            result_part1 += int(gameID)
            print('NEW RESULT ' + str(result_part1))
        counter += 1

    return result_part1



def solve_day2_part2(input_data):
    data = read_input_string(input_data)

    result_part2 = 0

    for line in data:
        result_part2 += fewest_cube_config(line)

    return result_part2

print(solve_day2_part2("../inputs/day2.txt"))

# # Example usage:
# input_str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# result = fewest_cube_config(input_str)
# print(result) # should be 48