# A function to get a list of num_fib_terms fibonacci numbers
def fibonacci(num_fib_terms):
    # Check lower bounds
    if num_fib_terms == 0:
        return []
    if num_fib_terms == 1:
        return [0]
    # Calculate the fib list
    fibs = [0, 1]  # Fib series always starts with [0, 1]
    for _ in range(2, num_fib_terms):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
