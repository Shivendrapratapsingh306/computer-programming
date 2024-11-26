# Question: How do you create a function that accepts any number of keyword arguments?
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Alice", age=25, city="New York")
