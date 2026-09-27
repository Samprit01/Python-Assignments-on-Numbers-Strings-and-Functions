def last_character(text: str):
    print(f"Using index: {text[-1]}")
    
    last = ""
    for _ in text:
        last = _ 
    print(f"Using loop: {last}")

text = input('Enter a string: ')
last_character(text)