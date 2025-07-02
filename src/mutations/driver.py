from src.mutations.util import mutate_string

if __name__ == '__main__':
    string = input("Enter the original string: ")
    position, character = input("Enter the position and new character (space-separated): ").split()

    new_string = mutate_string(string, int(position), character)
    print(new_string)