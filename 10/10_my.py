case1 = "[](){}" # 3
case2 = "}]()[{" # 2
case3 = "[)(]" # 0
case4 = "}}}" # 0
case5 = "({)}" # 0

def solution(param_str):
    count = 0
    pair = {']': '[', '}': '{', ')': '('}
    
    for _ in range(len(param_str)):
        stack = []
        is_valid = True
        
        for char in param_str:
            if char in "[{(":
                stack.append(char)
            else:
                if not stack or stack.pop() != pair[char]:
                    is_valid = False
                    break
        
        if is_valid and not stack:
            count += 1
            
        param_str = param_str[1:] + param_str[0]
        
    return count


print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))
print(case4, "->", solution(case4))
print(case5, "->", solution(case5))