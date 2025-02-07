def print_numbers(n, current=1):
    if current > n:
        return  # Base case: Stop when current exceeds N
    print(current)
    print_numbers(n, current + 1)  # Recursive call with incremented value

# Example usage
print_numbers(5)  # Output: 1 2 3 4 5
