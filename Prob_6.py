import string

input_str_1 = "abcdefghijklmnopqrstuvwxyz"
input_str_2 = "The quick brown fox jumps over the lazy dog"
input_str_3 = "Hello"

def pangram(input_str):
    alphabet = set(string.ascii_lowercase)
    input_str_lower = input_str.lower()
    input_set = set(input_str_lower)
    return alphabet.issubset(input_set)

print(pangram(input_str_1))
print(pangram(input_str_2))
print(pangram(input_str_3))