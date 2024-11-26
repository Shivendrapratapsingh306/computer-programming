# Question: How do you get the value of a key with a default if the key does not exist?
my_dict = {"name": "Alice", "age": 25}
value = my_dict.get("city", "Unknown")
print(value)
