case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(answers):
    # A, B, C 한 명에 대한 찍기 패턴
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    # 정답 List(len: patterns의 길이와 동일 ? 3명이니)
    correct = [0] * len(patterns)

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                correct[j] += 1
    print(f"correct: {correct}")
    max_val = max(correct)
    result = []
    
    for i in range(len(correct)):
        if correct[i] == max_val:
            result.append(i+1)
    
    return result

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))