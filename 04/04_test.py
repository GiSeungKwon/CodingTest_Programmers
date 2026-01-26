case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(answers):
    patterns =[
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    correct = [0 for _ in range(len(patterns))]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                correct[j] += 1
    
    return_list = {}
    max_value = max(correct)
    for i, item in enumerate(correct):
        if max_value == item:
            return_list[i+1] = item

    return sorted(return_list, key=lambda x:return_list[x])        

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))