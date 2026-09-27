def first_character(text: str):
    for _ in text:
        print(f"First character: {_}")
        break 
text = input('Enter a string: ')
first_character(text)