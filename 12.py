def unique_elements(input_list):
    # Using method #2 (ordered and efficient)
    return list(dict.fromkeys(input_list))

# Example usage
if __name__ == "__main__":
    sample = [3, 1, 2, 2, 4, 3, 5, 1]
    print("Original list:", sample)
    print("Unique elements:", unique_elements(sample))
