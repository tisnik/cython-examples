def fibonacci(n):
    a, b = 1, 1
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1
    return a


for i in range(0, 41):
    print(fibonacci(i))
