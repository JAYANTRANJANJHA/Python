# Sample dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'occupation': 'Engineer'
}

# Function to check key existence
def check_key(dictionary, key):
    if key in dictionary:
        return f"Key '{key}' exists with value: {dictionary[key]}"
    else:
        return f"Key '{key}' does not exist in the dictionary"

# Get user input
user_key = input("Enter a key to check: ")

# Check and display result
print(check_key(my_dict, user_key))
