def remove_first_occurrence(input_string):
    seen_chars = set()
    result = []
    
    for char in input_string:
        if char.lower() not in seen_chars and char.upper() not in seen_chars:
            seen_chars.add(char)
        else:
            result.append(char)
    
    return ''.join(result)

# Get input from user
user_input = input("Enter a string: ")

# Process and display result
output = remove_first_occurrence(user_input)
print(f"String after removing first occurrences: {output}")
