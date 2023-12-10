# Solution for Advent of Code 2023 Day 1, "Trebuchet?!"
# https://adventofcode.com/2023/day/1

from pathlib import Path

FILEPATH = Path.cwd() / '01-calibration' / 'input.txt'

input_lines = []
left_digit = 0
right_digit = 0
calibration_sum = 0

# load input text file into a list with each line as one list item
with open(FILEPATH) as input_file:
    for line in input_file:
        input_lines.append(line)

# for each item in the list:
    # find the leftmost digit
    # find the rightmost digit
    # make a two-digit number out of them
    # add that two-digit number to the running total

def get_left_digit(foo):
    for char in range(0, (len(foo)-1)):
        if foo[char].isdecimal() is True:
            return foo[char]

def get_right_digit(bar):
    for char in range((len(bar)-1), -1, -1):
        if bar[char].isdecimal() is True:
            return bar[char]

for item in input_lines:
    left_digit = get_left_digit(item)
    right_digit = get_right_digit(item)
    calibration_item = int(left_digit + right_digit)
    calibration_sum = calibration_sum + calibration_item
            
# return the final total
print(calibration_sum)
    