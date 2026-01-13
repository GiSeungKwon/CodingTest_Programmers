# N: 5 stages: [2,1,2,6,2,4,3,3]
def solution(N, stages):
    challengers = [0] * (N+2)
    for stage in stages:
        challengers[stage] += 1 # [0, 1, 3, 2, 1, 0, 1, 0]
    fails = {}
    total = len(stages)
    for i in range(1, N+1):
        if challengers[i] == 0:
            fails[i] = 0
        else:
            fails[i] == challengers[i] / total
            total -= challengers[i]
    result = sorted(fails, key=lambda x: fails[i], reverse=True)
    return result
print(solution(5, [2,1,2,6,2,4,3,3]))