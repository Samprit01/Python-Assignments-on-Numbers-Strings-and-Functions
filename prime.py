def check_prime(n):
    if n==1:
        return False

    for _ in range(2, n):
        if n % _ == 0:
            return False
    return True

n = int(input('Enter a number: '))
if check_prime(n):
    print('Prime')
else:
    print('Not Prime')