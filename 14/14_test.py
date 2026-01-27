case1_1,case1_2,case1_3 = 8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] #"OOOOXOOO"
case2_1,case2_2,case2_3 =8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] #"OOXOXOOO"

def solution(n, k, cmds):
    stack = []
    answer = ["O" for _ in range(n)]
    Llist = [[i-1, i, i+1] for i in range(n)]
    Llist[0][0] = None
    Llist[-1][2] = None
    
    print(f"answer:{answer} Llist:{Llist}")
    for cmd in cmds:
        
        if cmd == "C":
            answer[k] = "X"
            pre, now, next = Llist[k]
            stack.append((pre, now, next))
            if pre is not None:
                Llist[pre][2] = next
            if next is not None:
                Llist[next][0] = pre
                k = next
            else:
                k = pre
        
        elif cmd == "Z":
            pre, now, next = stack.pop()
            answer[now] = "O"
            if pre is not None:
                Llist[pre][2] = now
            if next is not None:
                Llist[next][0] = now

        else:
            direction, x = cmd.split(" ")
            for i in range(int(x)):
                k = Llist[k][0] if direction == "U" else Llist[k][2]
    return "".join(answer)

print(case1_1,case1_2,case1_3)
print(solution(case1_1,case1_2,case1_3))

# print(case2_1,case2_2,case2_3)
# print(solution(case2_1,case2_2,case2_3))