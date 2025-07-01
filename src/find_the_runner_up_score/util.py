def find_runner_up_score(n, score_list):
    unique_scores = list(set(score_list))
    unique_scores.sort(reverse=True)
    if len(unique_scores) < 2:
        return "No runner-up"
    return unique_scores[1]
