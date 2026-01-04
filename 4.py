numbers = []
print("Enter 4 numbers:")

# Get 4 numbers from user
for i in range(4):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

# Initialize max and second_max
max_num = second_max = float('-inf')

# Find max and second max using loop
for num in numbers:
    if num > max_num:
        second_max = max_num  # Current max becomes second max
        max_num = num        # Update max with new value
    elif num > second_max and num != max_num:
        second_max = num      # Update second max

# Handle case where all numbers are equal
if second_max == float('-inf'):
    second_max = max_num

# Display results
print(f"\nMaximum number: {max_num}")
print(f"Second maximum number: {second_max}")
