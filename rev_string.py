def reverse_string_loop(text: str) -> str:
    rev = ""
    for char in text:
        rev = char + rev
    return rev

def reverse_string_slice(text: str) -> str:
    return text[::-1]

text = input('Enter a string: ')
print(f"Approach 1 (Loop): {reverse_string_loop(text)}")
print(f"Approach 2 (Slice): {reverse_string_slice(text)}")