# [1,-5,2,4,3] [-5,1,2,4,3]
# [2,1,1,3,2,5,4] [1,1,2,2,3,4,5]
# [6,1,7] [1,6,7]
def solution(param_list):
    return sorted(param_list)

print(solution([1,-5,2,4,3]))
print(solution([2,1,1,3,2,5,4]))
print(solution([6,1,7]))