from src.min_and_max.util import min_then_max

if __name__ == '__main__':
    # Prompt user to enter dimensions
    n, m = map(int, input("Enter number of rows and columns (space-separated): ").split())

    # Read matrix input
    print(f"Enter {n} rows with {m} integers each:")
    data = [list(map(int, input().split())) for _ in range(n)]

    # Compute and print result
    result = min_then_max(data)
    print("Result:", result)
