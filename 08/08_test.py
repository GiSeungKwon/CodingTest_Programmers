case1 = "(())()" # True
case2 = "((())()" # False
case3 = ")()()()" # False

def solution(str):
    print(str)
    stack = []
    pair = {")":"("}
    for char in str:
        if char in "({[":
            print(f"{char} -> stack:{stack} ", end="-> ")
            stack.append(char)
            print(f"stack.append({char}) -> stack:{stack}")
        else:
            if not stack or not(stack[-1] == pair[char]):
                if not not stack:
                    print(f"{char} -> stack:{stack} not stack:{not stack} stack[-1]{stack[-1]} != char{char}: {stack[-1] != char} -> return False")
                return False
            else:
                print(f"else -> stack:{stack} stack.pop() ", end="-> ")
                stack.pop()
                print(f"stack:{stack}")
    return True if not stack else False

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))
print(case3, "->", solution(case3))