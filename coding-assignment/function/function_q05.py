# Question: How do you create a function that accepts any number of positional arguments?
def sum_all(*numbers):
    return sum(numbers)
result = sum_all(1, 2, 3, 4, 5)
print(result)
