# Get input from user
numbers = input("Enter numbers separated by spaces: ")

# Convert input string to list of floats
try:
    num_list = [float(num) for num in numbers.split()]
except ValueError:
    print("Please enter only numbers separated by spaces.")
    exit()

# Sort the numbers in ascending order
num_list.sort()

# Display the sorted list
print("Sorted numbers (ascending order):", num_list)
