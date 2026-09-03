input_1 = "Hello"
input_2 = "Coding"
input_3 = "Nora"

Prefix_1 = "He"
Prefix_2 = "Con"
Prefix_3 = "Circum"

def check_prefix(input_str, prefix):
    if len(prefix) > len(input_str):
        return False
    return input_str.startswith(prefix)

print(check_prefix(input_1, Prefix_1))
print(check_prefix(input_2, Prefix_2))
print(check_prefix(input_3, Prefix_3))