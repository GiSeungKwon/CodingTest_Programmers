# [2,1,3,4,1] [2,3,4,5,6,7]
# [5,0,2,7] [2,5,7,9,12]
def solution(param_list):
    result = []
    for i in range(len(param_list)):
        for j in range(i+1, len(param_list)):
            result.append(param_list[i]+param_list[j])
    return sorted(set(result))

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))