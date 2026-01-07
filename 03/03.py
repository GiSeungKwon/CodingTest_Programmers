import ast

def to_list(param_input):
    return ast.literal_eval(param_input)

def calc_sum(param_list):
    result = []
    for i in range(len(param_list)):
        for j in range(len(param_list)):
            if i == j:
                continue
            result.append(param_list[i] + param_list[j])
    return result

def remove_duplication(param_list):
    return list(set(param_list))

def sort(param_list):
    return sorted(param_list)

def solution():
    # return sort(remove_duplication(calc_sum(to_list(input()))))
    return (lambda x : sort(remove_duplication(calc_sum(to_list(x)))))(input())
print(solution())