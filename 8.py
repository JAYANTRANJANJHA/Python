try:
    user_input = input("Enter a string to reverse: ")
    if not user_input:
        print("You didn't enter anything!")
    else:
        print(f"Reversed string: {user_input[::-1]}")
except Exception as e:
    print(f"An error occurred: {e}")
