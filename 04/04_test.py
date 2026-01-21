case1 = [1,2,3,4,5] # [1]
case2 = [1,3,2,4,2] # [1,2,3]

def solution(param_list):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    correct = [0 for _ in range(len(patterns))]
    for answer_index, answer in enumerate(param_list):
        for pattern_index, pattern in enumerate(patterns):
            print(f"answer:{answer} pattern_index:{pattern_index} pattern:{pattern} - {pattern[answer_index%len(patterns[pattern_index])]}")
            if answer == pattern[answer_index%len(patterns[pattern_index])]:
                # print("same")
                correct[pattern_index] += 1
        print()
    return correct

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))