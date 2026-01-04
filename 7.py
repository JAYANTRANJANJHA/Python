def get_unique_elements(input_list):
    # Using Method 3 (preserves order and works for all Python versions)
    return list(dict.fromkeys(input_list))

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    unique_elements = get_unique_elements(sample_list)
    print("Original list:", sample_list)
    print("Unique elements:", unique_elements)
