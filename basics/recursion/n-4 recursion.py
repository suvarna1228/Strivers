def print_numbers(n):
    if n <= 0:
        return  # Base case: Stop when n exceeds N
    print(n)
    print_numbers( n - 1)  # Recursive call with incremented value

# Example usage
print_numbers(5)  # Output: 1 2 3 4 5
