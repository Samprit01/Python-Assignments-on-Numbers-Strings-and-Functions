def remove_vowels(text: str) -> str:
    result = ""
    for char in text:
        if char.lower() not in 'aeiou':
            result += char
    return result

text = input('Enter a string: ')
print(f"Without vowels: {remove_vowels(text)}")