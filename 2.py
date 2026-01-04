# Get user's age
age = int(input("Please enter your age: "))

# Check voting eligibility
if age >= 18:
    print("You are eligible to vote in the next election!")
else:
    years_left = 18 - age
    print(f"You cannot vote yet. You'll be eligible in {years_left} year{'s' if years_left > 1 else ''}.")
