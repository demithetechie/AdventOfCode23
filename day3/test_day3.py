from utils import read_input
from day3.day3 import solve_day3_part1, solve_day3_part2

def test_day3_part1():
    input_data = read_input("../inputs/day3.txt") 
    expected_output = 42  
    assert solve_day3_part1(input_data) == expected_output

def test_day3_part2():
    input_data = read_input("../inputs/day3.txt") 
    expected_output = 123  
    assert solve_day3_part2(input_data) == expected_output