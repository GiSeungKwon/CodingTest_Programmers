# [1,2,3,4,5] [1]
# [1,3,2,4,2] [1,2,3]
def solution(param_list):
    patterns = [
        [ 1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    for i in range(len(param_list)):
        for j in range(len(patterns)):
            for k in range(len(patterns)%len(param_list))
    return

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))