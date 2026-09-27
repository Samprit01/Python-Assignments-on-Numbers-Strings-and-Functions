def remove_spaces(text: str) -> str:
    result = ""
    for char in text:
        if char != ' ':
            result = result + char
    return result

text = input('Enter a string: ')
print(f"Without spaces: {remove_spaces(text)}")