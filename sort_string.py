def sort_words(words):
    words_list = words.split()
    words_list = [word.lower() for word in words_list]
    return " ".join(sorted(words_list))


words = "apple chocolate ORANGE BABABA"
print(sort_words(words))