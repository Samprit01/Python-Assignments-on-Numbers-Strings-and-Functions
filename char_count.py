def count_characters(text: str) -> int:
    count = 0
    for _ in text:
        count = count + 1
    return count

text = input('Enter a string: ')
print(f"Characters: {count_characters(text)}")