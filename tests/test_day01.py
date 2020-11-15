from aoc2019.day01 import part_1, part_2, fuel_to_launch_mass

"""
For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
"""

def test_fuel_to_launch_mass_1():
    assert fuel_to_launch_mass(12) == 2

def test_fuel_to_launch_mass_2():
    assert fuel_to_launch_mass(14) == 2

def test_fuel_to_launch_mass_3():
    assert fuel_to_launch_mass(1969) == 654

def test_part_1():
    assert part_1([12, 14]) == 4