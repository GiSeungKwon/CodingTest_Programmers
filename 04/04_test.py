case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(param_list):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    count_correct = [0 for _ in range(len(patterns))]
    for i, answer in enumerate(param_list):
        for j, pattern in enumerate(patterns):
            if(answer == pattern[i % len(pattern)]):
                count_correct[j] += 1

    result = []
    max_value = max(count_correct)
    for i, count in enumerate(count_correct):
        if count == max_value:
            result.append(i+1)
    return result

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))