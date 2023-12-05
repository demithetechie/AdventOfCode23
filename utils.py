### helpful functions to process input data :)

# read input data from textfile as int in a list
def read_input_int(textfile):
    with open(textfile) as f:
        input_data = [int(line) for line in f]
    return input_data

# read input data from textfile as string in a list
def read_input_string(textfile):
    with open(textfile) as f:
        input_data = [line.strip() for line in f]
    return input_data

# read input data from textfile as string in a list, space separated
def read_input_space(textfile):
    with open(textfile) as f:
        input_data = [i.split(" ") for i in f]
    return input_data

# read input data from textfile as string in a list, comma separated
def read_input_char(textfile):
    with open(textfile) as f:
        input_data = [list(line.strip()) for line in f]
    return input_data

