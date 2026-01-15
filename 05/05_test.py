case1_1, case1_2 = [[1,4],[3,2],[4,1]], [[3,3],[3,3]] # [[15,15],[15,15],[15,15]]
case2_1, case2_2 = [[2,3,2],[4,2,4],[3,1,4]], [[5,4,3],[2,4,1],[3,1,1]] # [[22,22,11],[36,28,18],[29,20,14]]
def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result

print(solution(case1_1, case1_2))
print(solution(case2_1, case2_2))