def reverse_words(text:str) -> str: return ' '.join([word[::-1] for word in text.split()])

print(reverse_words('mi mama me mima'))