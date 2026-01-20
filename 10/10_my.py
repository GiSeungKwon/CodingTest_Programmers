case1 = 10 # 1010
case2 = 27 # 11011
case3 = 12345 # 11000000111001
case4 = 0
case5 = 1
case6 = 2

def solution(param_int):
    result = []
    while not param_int//2 == 0:
        result.append(str(param_int%2))
        param_int //= 2
    result.append(str(param_int % 2))
    return "".join(result[::-1])
    # return "".join(reversed(result))

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))
print(case6, "->", solution(case6))