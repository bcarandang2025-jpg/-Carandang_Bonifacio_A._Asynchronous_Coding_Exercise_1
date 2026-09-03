word = "Hello"
numbers = "4567"
mixed = "Hello59"
blank = ""

def only_digits(s):
    return s.isdigit()

print(only_digits(word))    
print(only_digits(numbers))  
print(only_digits(mixed))   
print(only_digits(blank))   