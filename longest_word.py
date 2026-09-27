def find_longest_word(text: str) -> str:
    longest = ""
    current = ""
    text = text + " "  
    for char in text:
        if char != ' ':
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
            
    return longest

text = input('Enter a sentence: ')
print(f"Longest word: {find_longest_word(text)}")