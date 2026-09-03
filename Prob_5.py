input_char1 = "Hello"
input_char2 = "World"
input_char3 = "Python"
input_char4 = "Python"

current_char1 = "l"
current_char2 = "W"
current_char3 = "P"
current_char4 = "x"

new_char1 = "s"
new_char2 = "A"
new_char3 = "x"
new_char4 = "a"

def replace_character(string, current_char, new_char):
    return string.replace(current_char, new_char)


print(replace_character(input_char1, current_char1, new_char1))
print(replace_character(input_char2, current_char2, new_char2))
print(replace_character(input_char3, current_char3, new_char3))
print(replace_character(input_char4, current_char4, new_char4))