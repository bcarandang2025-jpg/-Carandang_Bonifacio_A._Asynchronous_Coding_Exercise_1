# Problem 4: Remove Character at Specific Index

s = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

# Check if the string is empty or index is out of range
if s == "" or n < 0 or n >= len(s):
    print("Output:", s)
else:
    # Remove the character at index n
    result = s[:n] + s[n+1:]
    print("Output:", result)