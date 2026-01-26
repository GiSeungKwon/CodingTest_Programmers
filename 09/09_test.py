case0 = 28
case1 = 10 # 1010
case2 = 27 # 11011
case3 = 12345 # 11000000111001
case4 = 0 # 0
case5 = 1 # 1
case6 = 2 # 10

def solution(decimal):
    binary = ""
    while decimal // 2 != 0:
        binary += str(decimal%2)
        decimal //= 2
    binary += "1" if decimal%2==1 else "0"
    return binary[::-1]

print(case0, "->", solution(case0))
print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))
print(case6, "->", solution(case6))