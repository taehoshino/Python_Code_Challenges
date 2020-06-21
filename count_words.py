import string
from collections import Counter


def count_words(input_file):
    with open(input_file, "r") as f:
        punc = string.punctuation.replace("'","").replace("-","") # punctuations to be excluded
        input_text = f.read().lower()
        for ch in punc:
            input_text = input_text.replace(ch, "") # remove punctuations
        word_list = input_text.split()
        words_count = Counter(word_list)
        print(f"Total word counts: {len(word_list)}")
        print("\nTop 20 words")
        for i, top in enumerate(words_count.most_common(20)):
            print(f"{i+1}:\t{top[0]}\t{top[1]} (words)")


count_words("word_count_test.txt")