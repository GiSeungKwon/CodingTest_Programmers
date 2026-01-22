case1 = "(())()" # 7
case2 = "((())()" # 7
case3 = ")()()()"

def solution(str):
    stack = []
    for char in str:
        if char == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            stack.pop()
    if not stack:
        return True
    else:
        return False

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))