def sum_of_first_n(n):
    if n == 1:  # Base case
        return 1
    return n + sum_of_first_n(n - 1)  # Recursive case

# Example usage
print(sum_of_first_n(10))  # Output: 55
