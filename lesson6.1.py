import string
user_input = input("start-end: ")
start, end = user_input.split('-')

start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)

print(string.ascii_letters[start_index : end_index + 1])