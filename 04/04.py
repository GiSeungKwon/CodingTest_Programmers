import ast

def to_list(param_text):
    return ast.literal_eval(param_text)

def make_pattern(param_list):
    answer_len = len(param_list)

    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    person1 = person1 * ((answer_len // len(person1)) + 1)
    person1 = person1[:answer_len]

    person2 = person2 * ((answer_len // len(person2)) + 1)
    person2 = person2[:answer_len]

    person3 = person3 * ((answer_len // len(person3)) + 1)
    person3 = person3[:answer_len]
    return param_list, person1, person2, person3

def count_correct(answer, person1, person2, person3):
    count_correct_list = [0, 0, 0]
    for i in range(len(answer)):
        if answer[i] == person1[i]:
            count_correct_list[0] += 1
        if answer[i] == person2[i]:
            count_correct_list[1] += 1
        if answer[i] == person3[i]:
            count_correct_list[2] += 1
        print()
    return count_correct_list

def return_index(param_count_correct_list):
    max_value = max(param_count_correct_list)
    result = []
    for i in range(len(param_count_correct_list)):
        if param_count_correct_list[i] == max_value:
            result.append(i+1)
    return result

def solution():
    answer, person1, person2, person3 = make_pattern(to_list(input()))
    return return_index(count_correct(answer, person1, person2, person3))

print(solution())