case1_1,case1_2,case1_3 = 8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] #"OOOOXOOO"
case2_1,case2_2,case2_3 =8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] #"OOXOXOOO"

def solution(n, k, cmds):
    result = ["O"] * n
    Llist = [[i-1, i, i+1] for i in range(n)]
    Llist[0][0] = None
    Llist[-1][-1] = None
    print(f"Llist:{Llist}")
    stack = []

    for cmd in cmds:
        print(f"cmd:{cmd}",end=" ")
        if cmd == "C":
            stack.append(k)
            print(f"  stack.append({k})->stack:{stack}")
            result[k] = "X"
            print(f"  result[{k}]='X' -> result:{result}")
            pre, now, next = Llist[k]
            print(f"  pre:{pre} now:{now} next:{next} Llist[{k}]:{Llist[k]}")

            if pre is not None:
                print(f"    pre:{pre} is not None")
                Llist[pre][-1] = next
                print(f"      Llist[pre][-1]:{Llist[pre][-1]} = next:{next}")

            if next is not None:
                print(f"    next:{next} is not None")
                Llist[next][0] = pre
                print(f"      Llist[next][0]:{Llist[next][0]} = pre:{pre}")
                k = next
            else:
                print(f"    k:{k} -> k = pre:{pre}", end = " ")
                k = pre
                print(f"k:{k}")
            print(f"        Llist:{Llist} k:{k}")
            print()

        elif cmd == "Z":
            idx = stack.pop()
            print(f"  idx:{idx} = stack.pop()")
            result[idx] = "O"
            print(f"  result[idx]:{result[idx]} = 'X' result:{result}")
            pre, now, next = Llist[idx]
            print(f"  pre:{pre} now:{now} next:{next} Llist[{idx}]:{Llist[idx]}")
            if pre is not None:
                print(f"    if pre:{pre} is not None:")
                Llist[pre][-1] = now
                print(f"      Llist[pre][-1]:{Llist[pre][-1]} = now:{now}")
            if next is not None:
                print(f"    if next:{next} is not None:")
                Llist[next][0] = now
                print(f"      Llist[next][0]:{Llist[next][0]} = pre:{pre}")
            print()

        else:
            direct, x = cmd.split(" ")
            print(f" k:{k}",end=" -> ")
            if direct == "D":
                for _ in range(int(x)):
                    k = Llist[k][-1]
                    print(f"k:{k}", end=" -> ")
            else:
                for _ in range(int(x)):
                    k = Llist[k][0]
                    print(f"k:{k}", end=" -> ")
            print()
        print()
    return "".join(result)

print(case1_1,case1_2,case1_3)
print(solution(case1_1,case1_2,case1_3))

# print(case2_1,case2_2,case2_3)
# print(solution(case2_1,case2_2,case2_3))