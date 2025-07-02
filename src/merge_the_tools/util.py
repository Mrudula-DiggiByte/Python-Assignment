def merge_the_tools(string, k):
    string_split = [string[i:i + k] for i in range(0, len(string), k)]

    for word in string_split:
        seen = []
        for letter in word:
            if letter not in seen:
                seen.append(letter)
        print("".join(seen))