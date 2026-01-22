case0 = 28
case1 = 10 # 1010
case2 = 27 # 11011
case3 = 12345 # 11000000111001
case4 = 0
case5 = 1
case6 = 2

def solution(integer):
    binary = []
    while integer // 2 != 0:
        binary.append(str(integer%2))
        # print(f"integer:{integer} -> ", end="")
        integer //= 2
        # print(f"integer:{integer} - {binary[-1]}")
    if integer % 2 == 0:
        binary.append("0")
    else:
        binary.append("1")
    # print(f"integer:{integer} - {binary[-1]}")
    # print(binary)
    return "".join(binary[::-1])
    # return "".join(reversed(binary))

print(case0, "->", solution(case0))
print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))
print(case6, "->", solution(case6))