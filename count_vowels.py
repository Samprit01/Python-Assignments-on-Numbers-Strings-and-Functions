def count_each_vowel(text: str):
    a = e = i = o = u = 0
    for char in text.lower():
        if char == 'a': a += 1
        elif char == 'e': e += 1
        elif char == 'i': i += 1
        elif char == 'o': o += 1
        elif char == 'u': u += 1
        
    print(f"a={a}\ne={e}\ni={i}\no={o}\nu={u}")

text = input('Enter a string: ')
count_each_vowel(text)