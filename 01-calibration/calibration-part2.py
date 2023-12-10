# Solution for Advent of Code 2023 Day 1, "Trebuchet?!"
# https://adventofcode.com/2023/day/1

from pathlib import Path

FILEPATH = Path.cwd() / '01-calibration' / 'input.txt'
NUM_DICT = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

input_lines = []
alpha_list = []
left_digit = 0
right_digit = 0
calibration_sum = 0

# load input text file into a list with each line as one list item
with open(FILEPATH) as input_file:
    for line in input_file:
        input_lines.append(line)

def get_left_digit(foo):
    for char in range(0, (len(foo)-1)):
        if foo[char].isdecimal() is True:
            left_num = [int(foo[char]), char]

    for key in NUM_DICT.keys():
        alpha_list.append(foo.find(key))
        alpha_list.append(key) # leftmost index of spelled out number, spelled out number
        leftiest_idx = [min(i) for i in alpha_list if i != '-1']

        idx = alpha_list.index(leftiest_idx)
        leftiest_word = alpha_list[int(idx+1)]

    if left_num[1] < leftiest_idx:
        return left_num[0]
    else:
        return leftiest_word

        
    

def get_right_digit(bar):
    for char in reversed(range((len(bar)-1), -1, 1)):
        if bar[char].isdecimal() is True:
            return bar[char]

for item in input_lines:
    left_digit = get_left_digit(item)
    right_digit = get_right_digit(item)
    calibration_item = int(left_digit + right_digit)
    calibration_sum = calibration_sum + calibration_item
            
# return the final total
print(calibration_sum)
    