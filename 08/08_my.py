case1 = "(())()" # 7
case2 = "((())()" # 7
case3 = ")()("
def solution(param_text):
    stack = []
    for i, item in enumerate(param_text):
        if item == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))