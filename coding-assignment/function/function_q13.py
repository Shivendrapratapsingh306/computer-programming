# Question: How do you write a function to check if a string is a palindrome?
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome("madam"))
print(is_palindrome("hello"))
