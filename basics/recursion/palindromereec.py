def is_palindrome(s):
    # Base case: if the string has 0 or 1 character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check first and last characters, and recurse on the rest
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

# Example usage
word = "madam"
print(is_palindrome(word))  # Output: True

word = "hello"
print(is_palindrome(word))  # Output: False
