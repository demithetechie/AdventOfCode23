## Day 1 Challenge

# will figure out how to import this later
def read_input_string(textfile):
    with open(textfile) as f:
        input_data = [line.strip() for line in f]
    return input_data


def solve_day1_part1(input_data):
    lines = read_input_string(input_data)

    result_part1 = 0

    for line in lines:
        head = 0
        tail = len(line) - 1

        while head < tail:
            if line[head].isdigit() and line[tail].isdigit():
                break
            else:
                if not line[head].isdigit():
                    head += 1
                
                if not line[tail].isdigit():
                    tail -= 1

        value = line[head] + line[tail]
        result_part1 += int(value)

    return result_part1

def solve_day1_part2(input_data):
    lines = read_input_string(input_data)
    
    result_part2 = 0

    longDigits = {
        'eight': '8',
        'three': '3',
        'seven': '7',
    }

    midDigits = {
        'four': '4',
        'five': '5',
        'nine': '9',
    }

    shortDigits = {
        'one': '1',
        'two': '2',
        'six': '6', 
    }

    for line in lines:
        print(line)

        for i in range(0, len(line)-1):
            segment = line[i:i+5]
            # print(segment)
            for key, value in longDigits.items():
                if key in segment:
                    ending = key[-1]
                    line = line.replace(key, value + ending)
                    print(line)
                    # print("replaced " + segment + " with " + value)
            for key, value in midDigits.items():
                if key in segment:
                    ending = key[-1]
                    line = line.replace(key, value + ending)
                    print(line)
                    # print("replaced " + segment + " with " + value)
            for key, value in shortDigits.items():
                if key in segment:
                    ending = key[-1]
                    line = line.replace(key, value + ending)
                    print(line)
                    # print("replaced " + segment + " with " + value)
        
        print(line)

        head = 0
        tail = len(line) - 1

        while head < tail:
            # print(line[head], line[tail])
            if line[head].isdigit() and line[tail].isdigit():
                break
            else:
                # print('something')
                if not line[head].isdigit():
                    # print('head isnt a digit')
                    head += 1
                
                if not line[tail].isdigit():
                    # print('tail isnt a digit')
                    tail -= 1

        value = line[head] + line[tail]
        print(value)
        result_part2 += int(value)

    return result_part2

print(solve_day1_part2("../inputs/day1.txt"))