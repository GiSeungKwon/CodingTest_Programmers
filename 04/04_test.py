case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(param_list):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    result = [0 for _ in range(len(patterns))]
    for i, item in enumerate(param_list):
        for j, jtem in enumerate(patterns):
            if item == jtem[i % len(jtem)]:
                result[j] += 1
    max_value = max(result)
    return_list = []
    for i, item in enumerate(result):
        if item == max_value:
            return_list.append(i+1)
    return return_list

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))