case0 = 28
case1 = 10 # 1010
case2 = 27 # 11011
case3 = 12345 # 11000000111001
case4 = 0 # 0
case5 = 1 # 1
case6 = 2 # 10

def solution(decimal):
    stack = []
    while(decimal // 2 != 0):
        stack.append(str(decimal%2))
        decimal //= 2
    if decimal % 2 == 1:
        stack.append("1")
    else:
        stack.append("0")
    return "".join(stack)[::-1]
    # return "".join(reversed(stack))

print(case0, "->", solution(case0))
print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))
print(case6, "->", solution(case6))