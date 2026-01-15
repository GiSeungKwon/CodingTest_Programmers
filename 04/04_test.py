case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(param_list):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    count_correct = [0 for _ in range(len(patterns))]
    for i in range(len(param_list)):
        for j in range(len(patterns)):
            idx = i % len(patterns[j])
            if param_list[i] == patterns[j][idx]:
                count_correct[j] += 1
    result = []
    max_value = max(count_correct)
    for i in range(len(patterns)):
        if max_value == count_correct[i]:
            result.append(i+1)
    return result

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))