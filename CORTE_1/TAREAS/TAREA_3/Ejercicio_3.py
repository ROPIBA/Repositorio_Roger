def fibonacci(n):
    fib_series = [0, 1]
    while len(str(fib_series[-1])) < n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series

digit_count = int(input("Ingrese la cantidad de dígitos para la serie de Fibonacci: "))
fibonacci_series = fibonacci(digit_count)

print(f"Serie de Fibonacci con al menos {digit_count} dígitos:")
for num in fibonacci_series:
    print(num)
