import ast


def to_list(param_str):
    return ast.literal_eval(param_str)


def calculate_correct(param_list):
    answers = param_list
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    result = [0] * 3
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                result[j] += 1
    return result


def return_correct_index(param_list):
    result = []
    max_value = max(param_list)
    for index, item in enumerate(param_list):
        if max_value == item:
            result.append(index+1)
    return result


def solution():
    return (lambda x: return_correct_index(calculate_correct(to_list(x))))(input())


print(solution())
