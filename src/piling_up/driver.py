from src.piling_up.util import is_piling_possible

if __name__ == '__main__':
    T = int(input("Enter number of test cases: "))

    for i in range(T):
        n = int(input(f"\nEnter number of cubes for test case {i + 1}: "))
        cubes = list(map(int, input("Enter cube sizes (space-separated): ").split()))

        result = is_piling_possible(cubes)
        print(result)