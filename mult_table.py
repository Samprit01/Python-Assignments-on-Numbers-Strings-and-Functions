def multiplication_table(n):
    for _ in range(1, 11):
        print(f"{n} * {_} = {n*_}")

n = int(input('Enter a number: '))
multiplication_table(n)