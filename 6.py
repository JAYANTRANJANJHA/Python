def max_difference(nums):
    if len(nums) < 2:
        return 0  # Return 0 if list has fewer than 2 elements
    
    min_num = nums[0]
    max_diff = nums[1] - nums[0]
    
    for num in nums[1:]:
        current_diff = num - min_num
        if current_diff > max_diff:
            max_diff = current_diff
        if num < min_num:
            min_num = num
    
    return max_diff if max_diff > 0 else 0

# Get input from user
input_str = input("Enter numbers separated by spaces: ")
try:
    numbers = [float(num) for num in input_str.split()]
    result = max_difference(numbers)
    print(f"Maximum difference is: {result}")
except ValueError:
    print("Please enter valid numbers separated by spaces.")
