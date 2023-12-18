# Solution for Advent of Code 2023 Day 1, "Trebuchet?!" Part 2
# https://adventofcode.com/2023/day/1

from pathlib import Path

FILEPATH = Path.cwd() / '01-calibration' / 'input.txt'
NUM_DICT = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
            'seven': 7, 'eight': 8, 'nine': 9}
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

input_lines = []
calibration_sum = 0

# load input text file into a list with each line as one list item
with open(FILEPATH) as input_file:
    for line in input_file:
        input_lines.append(line)

# for each item in the list:
    # find the leftmost digit & text number & index of each
    # figure out which of them is the leftmost and return that
    # repeat for the rightmost
    # make a two-digit number out of leftmost & rightmost
    # add that two-digit number to the running total


def get_digit(text, direction):
    """given a line of text and a direction (left or right), this function
    returns the integer value of the leftmost or rightmight number between
    0 and 9 found in the line of text, whether it appears as a numeric
    digit or a word.

    Args:
        _string_ text: a line of text
        _string_ direction: 'left' or 'right'

    Returns:
        _integer_: The integer value of the leftmost or rightmight number
        between 0 and 9 found in the line of text, whether it appears as
        a numeric digit or a word.
    """
    word_list = []
    first_num = []

    if direction == 'left':
        this_search = range(0, (len(text)-1))
    elif direction == 'right':
        this_search = reversed(range(0, (len(text)-1)))
    else:
        pass  # exception handling goes here

    # build first_num, a list with the index and integer value of the left or
    # rightmost digit based on the parameter chosen
    for char in this_search:
        if text[char].isdecimal() is True:
            first_num = [char, int(text[char])]
            break

    # build word_list, a list of wordnums, their leftmost index, and their
    # rightmost index in this text, e.g. [1, 'one', 7, 'one', 3, 'two',
    # 3, 'two'] -- here 'one' appears at index positions 1 and 7 and 'two'
    # appears only once at index position 3
    for key in NUM_DICT:
        if key in text:
            word_list.append(text.find(key))  # find leftmost index of numword
            word_list.append(key)
            word_list.append(text.rfind(key))  # find rightmost idx of numword
            word_list.append(key)
    print(word_list)
    # if no numwords were found, return the chosen digit
    if word_list == []:
        return first_num[1]

    # find indices of leftmost and rightmost numwords
    indices = [i for i in word_list if isinstance(i, int)]
    leftiest_word_idx = min(indices)
    rightiest_word_idx = max(indices)

    # return int for whichever is leftmost/rightmost, digit or word
    if direction == 'left':
        if leftiest_word_idx < first_num[0]:
            leftiest_word = word_list[(leftiest_word_idx + 1)]
            return NUM_DICT[leftiest_word]
        else:
            return first_num[1]
    elif direction == 'right':
        if rightiest_word_idx > first_num[0]:
            rightiest_word = word_list[(rightiest_word_idx + 1)]
            return NUM_DICT[rightiest_word]
        else:
            return first_num[1]
    else:
        pass  # exception handling here

for item in input_lines:
    left_digit = str(get_digit(item, 'left'))
    right_digit = str(get_digit(item, 'right'))
    calibration_item = int(left_digit + right_digit)
    calibration_sum = calibration_sum + calibration_item

# return the final total
print(calibration_sum)
