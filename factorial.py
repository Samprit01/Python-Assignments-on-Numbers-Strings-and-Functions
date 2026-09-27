def factorial(n):
    r = 1
    for _ in range(1, n + 1):
        r= r*_
    return r

n = int(input('Enter a number: '))
print(f"Factorial: {factorial(n)}")