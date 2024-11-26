# Question: How do you check if a number is an Armstrong number?
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(digit) ** power for digit in digits)
print(is_armstrong(153))
print(is_armstrong(123))
