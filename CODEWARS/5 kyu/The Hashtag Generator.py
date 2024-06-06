def generate_hashtag(s:str):
    if not s: return False
    words = '#'+''.join(word.capitalize() for word in s.split())
    return words if len(words) <= 140 else False

