"""
https://adventofcode.com/2019/day/1
"""
import math

from aoc2019.utilities import read_input_file

def format_input(inputs):
    return [float(x) for x in inputs]

def part_1(component_masses):
    total_fuel_required = 0
    for mass in component_masses:
        total_fuel_required += fuel_to_launch_mass(mass)
    return total_fuel_required

def part_2(component_masses):
    total_fuel_required = 0
    for mass in component_masses:
        fuel_required += fuel_to_launch_mass(mass)
        while fuel_required > 0:
            total_fuel_required += fuel_required
            fuel_required = fuel_to_launch_mass(fuel_required)
    return total_fuel_required

def fuel_to_launch_mass(mass):
    return math.floor(mass / 3.0) - 2.0


if __name__ == "__main__":
    puzzle_input = read_input_file("day01.txt")
    puzzle_input = format_input(puzzle_input)

    total_fuel_required = part_1(puzzle_input)
    print(f'Part 1 total fuel required: {total_fuel_required}')

    updated_fuel_required = part_2(puzzle_input)
    print(f'Part 2 total fuel required: {updated_fuel_required}')