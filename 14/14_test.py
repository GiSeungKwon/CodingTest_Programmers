case1_1,case1_2,case1_3 = 8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] #"OOOOXOOO"
case2_1,case2_2,case2_3 =8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] #"OOXOXOOO"

def solution(n, k, cmds):
    roll_back_stack = []
    not_deleted = ["O"] * n

    Llist = [[i-1,i,i+1] for i in range(n)]
    Llist[0][0] = None
    Llist[-1][-1] = None
    print(Llist)
    
    for cmd in cmds:
        # 삭제
        if cmd == "C":
            print(f"\tk:{k} cmd:{cmd}=[Delete]", end=" ")
            pre, now, next = Llist[k]
            print(f"\tLlist[{k}]:{Llist[k]} pre:{pre}, now:{now}, next:{next}", end=" ")
            not_deleted[now] = "X"
            print(f"\tnot_deleted[now]: = 'X' not_deleted:{not_deleted}", end=" ")
            roll_back_stack.append(now)
            print(f"\troll_back_stack.append({now}) roll_back_stack:{roll_back_stack}")
            if pre is not None:
                Llist[pre][-1] = next
            if next is not None:
                Llist[next][0] = pre
                k = next
            else:
                k = pre
            print(f"Llist: {Llist}")

        # Roll_Back
        elif cmd == "Z":
            roll_back_index = roll_back_stack.pop()
            print(f"roll_back_index:{roll_back_index}", end=" ")
            pre, now, next = Llist[roll_back_index]
            print(f"\tLlist[{roll_back_index}]:{Llist[roll_back_index]} pre:{pre}, now:{now}, next:{next}", end=" ")
            not_deleted[now] = "O"
            print(f"\tnot_deleted[now]: = 'O' not_deleted:{not_deleted}", end=" ")
            if pre is not None:
                Llist[pre][-1] = now
            if next is not None:
                Llist[next][0] = now
            print(f"Llist: {Llist}")
        
        # 방향 이동
        else:
            dir, x = cmd.split(" ")
            print(f"dir: {dir} x:{x} k:{k} ->")
            if dir == "U":
                for i in range(int(x)):
                    k = Llist[k][0]
                    print(f"k=Llist[{k}][0] : {k}")
            elif dir == "D":
                for i in range(int(x)):
                    k = Llist[k][2]
                    print(f"k=Llist[{k}][0] : {k}")

    return "".join(not_deleted)

print(case1_1,case1_2,case1_3)
print(solution(case1_1,case1_2,case1_3))

# print(case2_1,case2_2,case2_3)
# print(solution(case2_1,case2_2,case2_3))