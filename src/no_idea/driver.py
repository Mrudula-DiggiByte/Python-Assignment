from src.no_idea.util import calculate_happiness

if __name__ == '__main__':

    n, m = map(int, input("Enter number of elements and size of sets (n m): ").split())
    arr = list(map(int, input(f"Enter {n} space-separated array elements: ").split()))
    A = set(map(int, input(f"Enter {m} space-separated elements for Set A (liked): ").split()))
    B = set(map(int, input(f"Enter {m} space-separated elements for Set B (disliked): ").split()))
    happiness = calculate_happiness(arr, A, B)
    print("Final Happiness Score:", happiness)