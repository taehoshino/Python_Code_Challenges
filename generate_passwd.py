import secrets


def generate_passphrase(num_words):
    with open("diceware.wordlist.asc", "r") as file:
        lines = file.readlines()[:]
    print(lines)
    word_list = [line.split()[1] for line in lines]
    print(word_list)
    words = [secrets.choice(word_list) for i in range(num_words)]
    return " ".join(words)


words = generate_passphrase(8)
print(words)