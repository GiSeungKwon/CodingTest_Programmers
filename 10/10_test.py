case1 = "[](){}" # 3
case2 = "}]()[{" # 2
case3 = "[)(]" # 0
case4 = "}}}" # 0
case5 = "({)}" # 0



print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))