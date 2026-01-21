case1 = "[](){}" # 3
case2 = "}]()[{" # 2
case3 = "[)(]" # 0
case4 = "}}}" # 0
case5 = "({)}" # 0

def solution(param_str):
    pair = {"]":"[", "}":"{", ")":"("}
    count = 0
    for i in range(len(param_str)):
        # print(f"i:{i} param_str:{param_str}")
        result = []
        is_valid = True
        for char in param_str:
            if char in "[{(":
                result.append(char)
                # print(f"char:{char} result:{result}")
            else:
                if not result or result.pop() != pair[char]:
                    # print(f"char:{char} result:{result} - pair[{char}]: {pair[char]}")
                    is_valid = False
                    break
        if is_valid and not result:
            count += 1
        param_str = param_str[1:]+param_str[0]
    return count

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))