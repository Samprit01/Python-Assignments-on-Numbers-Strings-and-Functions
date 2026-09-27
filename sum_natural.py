def sum_natural(n):
    t = 0
    for _ in range(1,n+1):
        t=t+_
    return t

n = int(input('Enter n: '))
print(f"Sum of {n} numbers is: {sum_natural(n)}")