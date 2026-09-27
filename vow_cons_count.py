def count_vowels_consonants(text: str):
    v = 0
    c = 0
    for char in text:
        if char == ' ':
            continue
        if char.lower() in 'aeiou':
            v = v + 1
        else:
            c = c + 1
    print(f"Vowels: {v}")
    print(f"Consonants: {c}")

text = input('Enter a string: ')
count_vowels_consonants(text)