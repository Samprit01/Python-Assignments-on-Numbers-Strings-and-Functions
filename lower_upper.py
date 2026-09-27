def convert_uppercase(text: str) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
    return result

text = input('Enter a string: ')
print(f"Using upper(): {text.upper()}")
print(f"Using loop: {convert_uppercase(text)}")