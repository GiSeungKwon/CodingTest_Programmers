case1 = "[](){}" # 3
case2 = "}]()[{" # 2
case3 = "[)(]" # 0
case4 = "}}}" # 0
case5 = "({)}" # 0

def solution(str):
    count = 0
    pair = {")":"(", "}":"{", "]":"["}
    for i in range(len(str)):
        stack = []
        for char in str:
            is_valid = False
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack[-1] != pair[char]:
                    break
                else:
                    stack.pop()
                    is_valid = True
        if not stack and is_valid:
            count += 1
        str = str[1:]+str[0]
    return count

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))