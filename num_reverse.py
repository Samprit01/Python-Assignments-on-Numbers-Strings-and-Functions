def reverse_number(n):
    r = 0
    while n > 0:
        i = n % 10
        r = (r * 10) + i
        n = n // 10
    return r

n = int(input('Enter a number: '))
print(f"Reversed: {reverse_number(n)}")