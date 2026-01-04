import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

def get_valid_radius():
    """Prompt user for radius and validate input."""
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius > 0:
                return radius
            else:
                print("Radius must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Circle Area Calculator")
    radius = get_valid_radius()
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is: {area:.2f}")

if __name__ == "__main__":
    main()
