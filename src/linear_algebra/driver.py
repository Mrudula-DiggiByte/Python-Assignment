from src.linear_algebra.util import calculate_determinant

if __name__ == '__main__':
    n = int(input("Enter the size of the square matrix (n): "))
    print(f"Enter {n} rows with {n} float numbers:")
    matrix = [list(map(float, input().split())) for _ in range(n)]

    result = calculate_determinant(matrix)
    print("Determinant:", result)
