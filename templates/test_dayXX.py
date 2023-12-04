from utils import read_input
from dayXX import solve_dayXX 

def test_dayXX_part1():
    input_data = read_input("../inputs/dayXX.txt") 
    expected_output = 42  
    assert solve_dayXX(input_data) == expected_output

def test_dayXX_part2():
    input_data = read_input("../inputs/dayXX.txt") 
    expected_output = 123  
    assert solve_dayXX(input_data) == expected_output