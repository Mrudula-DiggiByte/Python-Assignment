from src.text_alignment.util import print_h_pattern

if __name__ == '__main__':
    thickness = int(input("Enter the thickness (odd number): "))
    if thickness % 2 == 0:
        print("Please enter an odd number.")
    else:
        print_h_pattern(thickness)