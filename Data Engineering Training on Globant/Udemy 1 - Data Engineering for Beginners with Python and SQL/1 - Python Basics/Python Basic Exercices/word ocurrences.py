def count_word_occurrences(text, word):
    if not text or not word: return 0
    return text.lower().count(word.lower())