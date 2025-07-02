from src.floor_ceil_and_rint.util import process_array

if __name__ == '__main__':
    user_input = list(map(float, input("Enter space-separated numbers: ").split()))
    process_array(user_input)