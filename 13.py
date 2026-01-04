def get_valid_input():
    """
    Continuously prompts the user until valid input is received.
    Returns the validated input.
    """
    while True:
        user_input = input("Please enter a number: ")
        try:
            # Try to convert input to a float (handles both integers and decimals)
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

def main():
    print("Number Validation Program")
    valid_number = get_valid_input()
    print(f"You entered a valid number: {valid_number}")

if __name__ == "__main__":
    main()
