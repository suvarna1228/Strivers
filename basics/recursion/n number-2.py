def print_name(n, name):
    if n <= 0:
        return  
    print(name)
    print_name(n - 1, name)  # Recursive call with n decremented


print_name(5, "Suvarna")
