# Question: How do you write a function to count the number of vowels in a string?
def count_vowels(string):
    vowels = "aeiou"
    return sum(1 for char in string.lower() if char in vowels)
print(count_vowels("hello world"))
