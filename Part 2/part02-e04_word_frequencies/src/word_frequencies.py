#!/usr/bin/env python3

def word_frequencies(filename):
    all_words = []
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            stripped_words = [i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in words]
            for word in stripped_words:
                all_words.append(word)
        word_set = set(all_words)
        word_dict = {}
        for word in word_set:
            word_dict[word] = all_words.count(word)
    return word_dict

def main():
    word_frequencies("src/alice.txt")

if __name__ == "__main__":
    main()
