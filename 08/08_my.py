case1 = "(())()" # 7
case2 = "((())()" # 7
case3 = ")()()()"

def solution(param_str):
    result = []
    for char in param_str:
        if char == "(":
            result.append("(")
        elif char == ")":
            if not result:
                return False
            result.pop()
    if result:
        return False
    else:
        return True

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))