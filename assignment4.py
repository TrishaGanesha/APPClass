def sum_n(n, result=0, level=0):
    print("  " * level + f"sum({n}, {result})")

    if n == 0:
        print("  " * level + f"Return: {result}")
        return result

    return sum_n(n - 1, result + n, level + 1)


n = int(input("Enter n: "))

result = sum_n(n)

print("\nSum =", result)


def factorial(n, result=1, level=0):
    print("  " * level + f"factorial({n}, {result})")

    if n == 0:
        print("  " * level + f"Return: {result}")
        return result

    return factorial(n - 1, result * n, level + 1)


n = int(input("Enter n: "))

result = factorial(n)

print("\nFactorial =", result)


def fibonacci(n, a=0, b=1, level=0):
    print("  " * level + f"fib({n}, {a}, {b})")

    if n == 0:
        print("  " * level + f"Return: {a}")
        return a

    return fibonacci(n - 1, b, a + b, level + 1)


n = int(input("Enter n: "))

result = fibonacci(n)

print("\nFibonacci number =", result)