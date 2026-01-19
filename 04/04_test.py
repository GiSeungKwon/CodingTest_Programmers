case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(param_list):
    answer = param_list
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    correct = [0 for _ in range(len(patterns))]
    print(f"correct: {correct}")

    # for i in range(len(answer)):
    #     for j in range(len(patterns)):
    #         if answer[i] == patterns[j][i%len(patterns[j])]:
    #             print(f"answer[{i}]:{answer[i]} == patterns[{j}][{i%len(patterns[j])}: {patterns[j][i%len(patterns[j])]}")
    #             correct[j] += 1
    # print(correct)

    for i, item in enumerate(answer):
        for j, jtem in enumerate(patterns):
            print(f"j: {i%len(jtem)} jtem: {jtem} jtem[{i%len(jtem)}]: {jtem[i%len(jtem)]}")
            if item == jtem[i%len(jtem)]:
                correct[j] += 1
            print(f"correct[{j}]: {correct[j]}")
    print(correct)

    result = []
    max_value = max(correct)
    print(f"max_value: {max_value}")
    for i, item in enumerate(correct):
        if max_value == item:
            result.append(i+1)
    return result

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))