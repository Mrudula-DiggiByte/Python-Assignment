from src.time_delta.util import time_delta

if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))

    for i in range(t):
        print(f"\nTest case {i+1}:")
        t1 = input("Enter time string 1: ")
        t2 = input("Enter time string 2: ")

        result = time_delta(t1, t2)
        print(f"Time difference (in seconds): {result}")