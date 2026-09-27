def character_frequency(text: str, ch: str) -> int:
    count = 0
    for char in text:
        if char == ch:
            count = count + 1
    return count

text = input('Enter text: ')
ch = input('Enter character: ')
print(f"Frequency: {character_frequency(text, ch)}")