# counting = []

# def count_ten(direction):

#     if direction == 'up':
#         count_range = range(0, 10)
#     elif direction == 'down':
#         count_range = reversed(range(0, 10))

#     for num in count_range:
#         counting.append(num)

# user_choice = input("Do you want to count 'up' to ten or 'down' from ten?")
# count_ten(user_choice)
# print(counting)


word_list = [8, 'one', 2, 'four']
indices = [i for i in word_list if isinstance(i, int)]
print(indices)
