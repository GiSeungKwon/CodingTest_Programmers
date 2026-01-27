case1_1,case1_2,case1_3 = 8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] #"OOOOXOOO"
case2_1,case2_2,case2_3 =8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] #"OOXOXOOO"

def solution(n, k, cmds):
    result = ["O" for _ in range(n)]
    stack = []
    for cmd in cmds:
        if cmd == "C":
            result[k] = "X"
            stack.append(k)
        elif cmd == "Z":
            # 제약 조건) 삭제한 행이 없을 때 Z가 명령되지 않는다.
            roll_back_idx = stack.pop()
            result[roll_back_idx] = "O"
            
        else:
            # 제약 조건) 표의 범위를 벗어나는 이동은 입력되지 않는다.
            dir, x = cmd.split(" ")
            if dir == "U":
                k -= int(x)
            elif dir == "D":
                k += int(x)
    return "".join(result)


# print(case1_1,case1_2,case1_3)
# print(solution(case1_1,case1_2,case1_3))

print(case2_1,case2_2,case2_3)
print(solution(case2_1,case2_2,case2_3))