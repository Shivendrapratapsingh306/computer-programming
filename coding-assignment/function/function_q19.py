# Question: How do you find the greatest common divisor (GCD) of two numbers using a function?
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))
