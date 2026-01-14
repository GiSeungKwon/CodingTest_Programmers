# [4,2,2,1,3,4] [4,3,2,1]
# [2,1,1,3,2,5,4] [5,4,3,2,1]
def solution(param_list):
    return sorted(set(param_list), reverse=True)

print(solution([4,2,2,1,3,4]))
print(solution([2,1,1,3,2,5,4]))