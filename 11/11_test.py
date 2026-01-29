case1 = "baabaa" # 1
case2 = "cdcd" # 0

def solution(str):
    stack=[]
    for char in str:
        if not stack:
            stack.append(char)
        else:
            if(stack[-1] == char):
                stack.pop()
            else:
                stack.append(char)
    return 1 if not stack else 0

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))