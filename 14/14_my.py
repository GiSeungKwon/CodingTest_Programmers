case1_1,case1_2,case1_3 = 8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] #"OOOOXOOO"
case2_1,case2_2,case2_3 =8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] #"OOXOXOOO"

def solution(n, k, cmds):
    # 1. 양방향 연결 리스트 초기화 {현재: [이전, 다음]}
    # 리스트 인덱스를 활용해 빠르게 접근하기 위해 배열을 사용합니다.
    linked_list = [[i - 1, i + 1] for i in range(n)]
    linked_list[0][0] = None        # 첫 번째 행의 이전은 없음
    linked_list[n - 1][1] = None    # 마지막 행의 다음은 없음
    print(f"linked_list:{linked_list}")

    answer = ["O"] * n
    stack = []  # 삭제된 노드 정보를 담을 스택

    for cmd in cmds:
        if cmd == "C":  # 삭제
            answer[k] = "X"
            prev, next = linked_list[k]
            stack.append((k, prev, next))
            
            # 연결 고리 수정 (나를 건너뛰게 만들기)
            if prev is not None:
                linked_list[prev][1] = next
            if next is not None:
                linked_list[next][0] = prev
                k = next  # 다음 행으로 이동
            else:
                k = prev  # 마지막 행이면 이전 행으로 이동
                
        elif cmd == "Z":  # 복구
            node, prev, next = stack.pop()
            answer[node] = "O"
            
            # 예전 앞뒤 사람들에게 다시 나를 연결
            if prev is not None:
                linked_list[prev][1] = node
            if next is not None:
                linked_list[next][0] = node
                
        else:  # 이동 (U/D)
            dir, x = cmd.split()
            x = int(x)
            # 연결 리스트를 타고 x번만큼 점프!
            for _ in range(x):
                k = linked_list[k][0] if dir == "U" else linked_list[k][1]

    return "".join(answer)


print(case1_1,case1_2,case1_3)
print(solution(case1_1,case1_2,case1_3))

# print(case2_1,case2_2,case2_3)
# print(solution(case2_1,case2_2,case2_3))