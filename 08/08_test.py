case1 = "(())()" # True
case2 = "((())()" # False
case3 = ")()()()" # False



print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))