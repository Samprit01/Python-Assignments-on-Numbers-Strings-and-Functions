def count_consonants(text: str) -> int:
    count = 0
    for char in text:
        if char.lower() not in 'aeiou':
            count = count + 1
    return count

text = input('Enter a string: ')
print(f"Consonants: {count_consonants(text)}")