def count_vowels(text: str) -> int:
    count = 0
    for char in text:
        if char.lower() in 'aeiou':
            count = count + 1
    return count

text = input('Enter a string: ')
print(f"Vowels: {count_vowels(text)}")