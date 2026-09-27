def count_case(text: str):
    u = l = d = s = 0
    for char in text:
        if char.isupper(): u += 1
        elif char.islower(): l += 1
        elif char.isdigit(): d += 1
        elif char == ' ': s += 1
    
    print(f"Uppercase: {u}")
    print(f"Lowercase: {l}")
    print(f"Digits: {d}")
    print(f"Spaces: {s}")

text = input('Enter a string: ')
count_case(text)