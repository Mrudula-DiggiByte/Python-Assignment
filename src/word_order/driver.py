from src.word_order.util import count_words


if __name__ == '__main__':
    n = int(input("Enter number of words: "))
    words = [input() for _ in range(n)]

    unique_count, frequencies = count_words(words)

    print(unique_count)
    print(frequencies)
