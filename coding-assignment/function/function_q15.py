# Question: How do you write a function to calculate the sum of digits of a number?
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
print(sum_of_digits(123))
