def count_words(text: str) -> int:
    w = 0
    
    for _ in range(len(text)):
        if text[_] != ' ':
            if _ == 0 or text[_-1] == ' ':
                w = w + 1
                
    return w

text = input('Enter a sentence: ')
print(f"Words: {count_words(text)}")