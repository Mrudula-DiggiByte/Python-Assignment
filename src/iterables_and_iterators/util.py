from itertools import combinations
def calculate_a_ratio(letters, k):
    combs = list(combinations(letters, k))
    count_with_a = sum(1 for comb in combs if 'a' in comb)
    ratio = count_with_a / len(combs)
    return round(ratio, 3)