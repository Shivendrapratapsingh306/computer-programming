# Question: How do you check if a list is sorted in ascending order?
def is_sorted(lst):
    return lst == sorted(lst)
print(is_sorted([1, 2, 3]))
print(is_sorted([3, 2, 1]))
