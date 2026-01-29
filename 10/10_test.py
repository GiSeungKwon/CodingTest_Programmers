case1 = "[](){}" # 3
case2 = "}]()[{" # 2
case3 = "[)(]" # 0
case4 = "}}}" # 0
case5 = "({)}" # 0

def solution(gwals):
    pair = {")":"(","}":"{","]":"["}
    count = 0

    for _ in range(len(gwals)):
        stack = []
        for gwal in gwals:
            flag = False
            if gwal in "({[":
                stack.append(gwal)
            else:
                if not stack:
                    break
                else:
                    if stack[-1] == pair[gwal]:
                        stack.pop()
                        flag = True
        if not stack and flag:
            count += 1
        gwals = gwals[1:]+gwals[0]
    return count

print(case1, "->", solution(case1), end="\n\n")
print(case2, "->", solution(case2), end="\n\n")
print(case3, "->", solution(case3), end="\n\n")
print(case4, "->", solution(case4), end="\n\n")
print(case5, "->", solution(case5), end="\n\n")