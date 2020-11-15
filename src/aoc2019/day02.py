"""
https://adventofcode.com/2019/day/2
"""

from aoc2019.utilities import read_input_file
from aoc2019.intcode_computer import IntcodeComputer

def format_input(inputs):
    return [int(x) for x in input.split(',')]

def part_01(intcode_program):
    pass

if __name__ == "__main__":
    puzzle_input = read_input_file("day02.txt")
    program = format_input(puzzle_input)

    result = part_01(program)
    print(f"Part 1 solution: {result}")