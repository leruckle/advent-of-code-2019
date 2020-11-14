import os

def read_input_file(input_file_name):
    with open(os.path.join('inputs', input_file_name)) as file:
        lines = file.readlines()
    return lines