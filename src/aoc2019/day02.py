"""
https://adventofcode.com/2019/day/2
"""

from aoc2019.utilities import read_input_file
from aoc2019.intcode_computer import IntcodeComputer

def format_input(inputs):
    return [int(x) for x in inputs.split(',')]

def part_01(intcode_program):
    fix_1202_error(intcode_program)
    computer = IntcodeComputer()
    result = computer.run(intcode_program)
    return result

def fix_1202_error(intcode_program):
    intcode_program[1] = 12
    intcode_program[2] = 2

def part_02(intcode_program):
    computer = IntcodeComputer()
    memory_array_size = len(intcode_program)
    for i in range(memory_array_size):
        for j in range(memory_array_size):
            intcode_program[1] = i
            intcode_program[2] = j
            result = computer.run(intcode_program)
            if result == 19690720:
                return f"{i}{j}"
    raise Exception("Could not determine correct inputs to program to produce 19690720")


if __name__ == "__main__":
    puzzle_input = read_input_file("day02.txt")
    program = format_input(puzzle_input)

    part01_result = part_01(program)
    print(f"Part 1 solution: {part01_result}")

    part02_result = part_02(program)
    print(f"Part 2 solution: {part02_result}")