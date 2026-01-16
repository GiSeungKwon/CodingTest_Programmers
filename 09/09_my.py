case1 = 10 # 1010
case2 = 27 # 11011
case3 = 12345 # 11000000111001
def solution(param_no):
    result = []
    while param_no // 2 > 0:
        print(f"param_no: {param_no} ", end="-> ")
        result.append(param_no % 2)
        print(f"result: {result}", end="-> ")
        param_no = param_no // 2
        print(f"param_no: {param_no} ")
    if param_no == 1:
        result.append(1)
    else:
        result.append(0)
    result_str = ""
    for i in range(len(result)):
        result_str += str(result.pop())
    return result_str

print(case1, "->", solution(case1), end="\n\n")
print(case2, "->", solution(case2), end="\n\n")
print(case3, "->", solution(case3), end="\n\n")