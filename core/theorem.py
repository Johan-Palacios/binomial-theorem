from math import factorial


def combination(n: int, k: int):
    if n == 0:
        raise ValueError("N no debe ser 0")
    return round((factorial(n) / (factorial(n - k) * factorial(k))))


def binomial_theorem(n, k, x, y):
    return combination(n, k) * x ** (n - k) * y ** (k)


if __name__ == "__main__":
    pass
