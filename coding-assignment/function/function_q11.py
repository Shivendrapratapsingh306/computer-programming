# Question: How do you write a function to check if a number is prime?
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))
