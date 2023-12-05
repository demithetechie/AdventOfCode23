# vector logic innit

def read_input_char(textfile):
    with open(textfile) as f:
        input_data = [list(line.strip()) for line in f]
    return input_data

def check_surrounding(grid):
    print(grid)


def solve_day3_part1(input_data):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    data = read_input_char(input_data)

    print(data)

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] not in numbers and data[i][j] != ".":
                print(data[i][j])
                print(str(i))
                print(str(j))
                topLine = [data[i-1][j-1], data[i-1][j], data[i-1][j+1]]
                midLine = [data[i][j-1], data[i][j], data[i][j+1]]
                botLine = [data[i+1][j-1], data[i+1][j], data[i+1][j+1]]

                grid = [topLine, midLine, botLine]

                indexes = []

                for k in range(0, 3):
                    for l in range(0, 3):
                        print(grid[k][l])
                        if grid[k][l] in numbers:
                            indexes.append([k-1, l-1])
                
                for index in indexes:
                    x = index[0]
                    y = index[1]
                    print('coordinates: ' + str(x) + ', ' + str(y))
                    print('array cords: ' + str(i) + ', ' + str(j))
                    number = data[i+x][i+y]
                    print('this is a number: ' + number)
                    if data[i-x][j-y-1] in numbers:
                        print('left')

            else:
                print("error")
    
    result_part1 = 0

    return result_part1

def solve_day3_part2(input_data):
    # data = read_input_string(input_data)

    result_part2 = 0

    return result_part2

solve_day3_part1("../inputs/day3.txt")