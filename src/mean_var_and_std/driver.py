from src.mean_var_and_std.util import process_matrix_stats

if __name__ == '__main__':
    n, m = map(int, input("Enter the number of rows and columns (e.g. 2 3): ").split())
    print(f"Enter {n} rows with {m} integers each:")
    data = [list(map(int, input().split())) for _ in range(n)]
    array = numpy.array(data)

    mean, var, std = process_matrix_stats(array)

    print("Mean (row-wise):")
    print(mean)
    print("Variance (column-wise):")
    print(var)
    print("Standard Deviation:")
    print(std)