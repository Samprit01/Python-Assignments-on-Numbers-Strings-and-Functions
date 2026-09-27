def display_position(text: str):
    for i in range(len(text)):
        print(f"Position {i}: {text[i]}")

text = input('Enter a string: ')
display_position(text)