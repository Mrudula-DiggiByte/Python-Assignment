from src.find_the_runner_up_score.util import find_runner_up_score

if __name__ == "__main__":
    n = int(input("Enter number of scores: "))
    score_list = list(map(int, input(f"Enter {n} space-separated scores: ").split()))

    result = find_runner_up_score(n, score_list)
    print(result)