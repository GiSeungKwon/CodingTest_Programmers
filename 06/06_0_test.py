case1_1, case1_2 = 5, [2,1,2,6,2,4,3,3] # [3,4,2,1,5]
case2_1, case2_2 = 4, [4,4,4,4,4] # [4,1,2,3]

def solution(n, stages):
    challengers = [0 for _ in range(n+2)]
    for i, item in enumerate(stages):
        challengers[item] += 1
    print(f"challengers: {challengers}")

    total = len(stages)
    fails = {}
    for i in range(1, len(challengers)-1):
        fails[i] = challengers[i] / total
        total -= challengers[i]

    return sorted(fails, key=lambda x : fails[x], reverse=True)

print(solution(case1_1, case1_2))
print()
print(solution(case2_1, case2_2))