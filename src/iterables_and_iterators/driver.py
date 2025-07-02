from src.iterables_and_iterators.util import calculate_a_ratio
if __name__ == '__main__':
    n = int(input("Enter total number of letters: "))
    letters = input("Enter the letters separated by space: ").split()
    k = int(input("Enter the size of combinations to choose: "))
    ratio = calculate_a_ratio(letters, k)
    print(f"{ratio:.3f}")