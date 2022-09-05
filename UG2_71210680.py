import timeit

def Fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

for i in range(1, 101):
    start = timeit.default_timer()
    Fibonacci_iterative(i)
    end = timeit.default_timer()
    print(f'Fibonacci Iteratif data {i}: {end-start} detik adalah: {Fibonacci_iterative(i)}')

print()

def Fibonacci_rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci_rekursif(n-1) + Fibonacci_rekursif(n-2)

for i in range(1, 101):
    start = timeit.default_timer()
    Fibonacci_rekursif(i)
    end = timeit.default_timer()
    print(f'Fibonacci rekursif data {i}: {end-start} detik adalah: {Fibonacci_rekursif(i)}')