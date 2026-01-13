# [2,1,3,4,1] [2,3,4,5,6,7]
def solution(param_list):
    param_list.sort()
    result = []
    for i in range(len(param_list)):
        for j in range(i+1, len(param_list)):
            result.append(param_list[i]+param_list[j])
    return sorted(list(set(result)))

print(solution([2,1,3,4,1]))