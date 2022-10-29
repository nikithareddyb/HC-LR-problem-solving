def stones(n, a, b):
    # Write your code here
    values = set()

    if a > b:
        a, b = b, a

    for i in range(n):
        values.add((i * a) + (n - 1 - i) * b)

    return sorted(list(values))