def calculate_happiness(arr, liked_set, disliked_set):
    happiness = 0
    for item in arr:
        if item in liked_set:
            happiness += 1
        elif item in disliked_set:
            happiness -= 1
    return happiness