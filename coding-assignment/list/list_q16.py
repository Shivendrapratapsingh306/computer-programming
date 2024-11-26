nested_lst = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested_lst for item in sublist]
print(flattened)
