# Question: How do you calculate the Fibonacci sequence using a function?
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
print(fibonacci(10))
