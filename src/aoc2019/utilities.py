import os

def read_input_file(input_file_name):
    with open(os.path.join('inputs', input_file_name)) as file:
        lines = file.readlines()
    if len(lines) == 1:
        lines = lines[0]
    return lines