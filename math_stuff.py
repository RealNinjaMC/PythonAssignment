def factorial(n):
    if n < 0:
        raise ValueError("Negative number not allowed")
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("Numbers must be non-negative")
    while b != 0:
        a, b = b, a % b
    return a
