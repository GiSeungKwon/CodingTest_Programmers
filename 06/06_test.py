case1_1, case1_2 = 5, [2,1,2,6,2,4,3,3] # [3,4,2,1,5]
case2_1, case2_2 = 4, [4,4,4,4,4] # [4,1,2,3]
case3_1, case3_2 = 6, [2,1,2,7,3,5,2,4] # [5,2,4,3,1,6]

def solution(n, stages):
    challengers = [0 for _ in range(n+2)]
    for item in stages:
        challengers[item] += 1
    print(f"challengers: {challengers}")
    fails = {}
    total = len(stages)
    for i in range(1, n+1):
        print(f"i:{i} {challengers[i]}/{total} challengers[{i}]:{challengers[i]} total:{total}")
        if total == 0:
            continue
        fails[i] = challengers[i] / total
        total -= challengers[i]
    return sorted(fails, key=lambda x: fails[x], reverse=True)


print(solution(case1_1, case1_2))
print(solution(case2_1, case2_2))
print(solution(case3_1, case3_2))