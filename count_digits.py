def count_digits(n:int) -> int:
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count = count + 1
        n = n // 10
    return count

n = int(input('Enter a number: '))
print(f"Digits: {count_digits(n)}")