from src.collections_namedtuple.util import calculate_average_marks

if __name__ == '__main__':
    N = int(input("Enter number of students: "))
    headers = input("Enter headers (e.g., ID MARKS NAME CLASS): ").split()
    data_rows = [input(f"Enter data for student {i+1}: ") for i in range(N)]

    result = calculate_average_marks(N, headers, data_rows)
    print(result)
