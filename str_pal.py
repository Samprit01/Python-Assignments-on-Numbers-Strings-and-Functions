def check_palindrome(text: str) -> bool:
    return text == text[::-1]

text = input('Enter a string: ')
if check_palindrome(text):
    print('Palindrome')
else:
    print('Not Palindrome')