def factorial(x):
    if x <= 1:
        return x
    return x * factorial(x - 1)


if __name__ == "__main__":
    a = 4
    print(factorial(a))