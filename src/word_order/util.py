from collections import Counter

def count_words(words):
    counter = Counter(words)
    unique_count = len(counter)
    frequencies = [str(counter[word]) for word in counter.keys()]
    return unique_count, " ".join(frequencies)