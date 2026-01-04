def divide_numbers():
    """
    Prompts the user for two numbers and performs division,
    handling potential exceptions gracefully.
    """
    print("Division Calculator")
    print("-------------------")
    
    try:
        # Get user input
        numerator = float(input("Enter the first number (numerator): "))
        denominator = float(input("Enter the second number (denominator): "))
        
        # Perform division
        result = numerator / denominator
        
        # Display result
        print(f"\nResult: {numerator} ÷ {denominator} = {result:.2f}")
    
    except ValueError:
        print("\nError: Please enter valid numbers only.")
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Division Calculator!")

# Run the program
if __name__ == "__main__":
    divide_numbers()
