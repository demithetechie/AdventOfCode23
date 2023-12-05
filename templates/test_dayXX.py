from utils import read_input
from dayXX import solve_dayXX_part1, solve_dayXX_part2

def test_dayXX_part1():
    input_data = read_input("../inputs/dayXX.txt") 
    expected_output = 42  
    assert solve_dayXX_part1(input_data) == expected_output

def test_dayXX_part2():
    input_data = read_input("../inputs/dayXX.txt") 
    expected_output = 123  
    assert solve_dayXX_part2(input_data) == expected_output