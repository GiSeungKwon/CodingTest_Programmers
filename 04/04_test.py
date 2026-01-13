# [1,2,3,4,5] [1]
# [1,3,2,4,2] [1,2,3]
def solution(param_list):
    patterns = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]
    result = [0 for _ in range(len(patterns))]

    # i = 정답 index
    for i in range(len(param_list)):
        # j = patterns index
        for j in range(len(patterns)):
            if param_list[i] == patterns[j][i%len(patterns[j])]:
                result[j] += 1
    result_idx = []
    max_value = max(result)
    for i in range(len(result)):
        if result[i] == max_value:
            result = tuple(result)
            result_idx.append(result.index(result[i]) + 1)
            result = list(result)
            result[i] = -1
    return result_idx

# print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
