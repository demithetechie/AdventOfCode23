from day1 import solve_day1_part1, solve_day1_part2

def test_day1_part1():
    expected_output = 142
    assert solve_day1_part1("../inputs/day1.txt") == expected_output

def test_day1_part2():
    expected_output = 281
    assert solve_day1_part2("../inputs/day1.txt") == expected_output

test_day1_part2()