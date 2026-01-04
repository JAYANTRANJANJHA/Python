# Get input from user
num = int(input("Enter a positive integer to calculate its factorial: "))

# Initialize factorial to 1
factorial = 1

# Calculate factorial using a loop
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
