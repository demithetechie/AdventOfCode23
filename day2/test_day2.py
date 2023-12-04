from utils import read_input
from day2.day2 import solve_day2_part1, solve_day2_part2

def test_dayXX_part1():
    input_data = read_input("../inputs/day2.txt") 
    expected_output = 42  
    assert solve_dayXX(input_data) == expected_output

def test_dayXX_part2():
    input_data = read_input("../inputs/day2.txt") 
    expected_output = 123  
    assert solve_dayXX(input_data) == expected_output