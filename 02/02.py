import ast

def to_list(param_text):
    return ast.literal_eval(param_text)

def reverse_sort(param_list):
    return sorted(param_list, reverse=True)

def remove_duplication(param_sorted_list):
    tmp = ""
    result = []
    for item in param_sorted_list:
        if tmp != item:
            tmp = item
            result.append(item)
    return result

def solution():
    # return remove_duplication(reverse_sort(to_list(input())))
    # return (lambda x: remove_duplication(reverse_sort(to_list(x))))(input())
    # return reverse_sort(set(to_list(input())))
    return (lambda x: reverse_sort(set(to_list(x))))(input())

print(solution())