def print_n_times(n):
    if n <= 0:
        return
    print("Hello, Recursion!")
    print_n_times(n - 1)
print_n_times(5)
