case1 = "(())()" # True
case2 = "((())()" # False
case3 = ")()()()" # False

def solution(gwalhos):
    stack = []
    pair = {")":"(","}":"{","]":"["}

    for gwalho in gwalhos:
        if gwalho in "({[":
            stack.append(gwalho)
        else:
            if not stack:
                return False
            else:
                if stack[-1] == pair[gwalho]:
                    stack.pop()
    return True if not stack else False

def solution(gwalhos):
    stack = []
    pair = {")":"(","}":"{","]":"["}

    for gwalho in gwalhos:
        if gwalho in "({[":
            stack.append(gwalho)
        else:
            if not stack:
                return False
            else:
                if stack[-1] == pair[gwalho]:
                    stack.pop()
    return True if not stack else False

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))