# 2차원 배열 board 5행(j) 5열(i)
board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]
# 인형을 집는 크레인을 작동시킨 위치가 담긴 배열 moves
moves = [1,5,3,5,1,2,1,4]
# 크레인을 모두 작동시킨 후 사라진 인형 개수를 반환

def solution(board, moves):
    stack = []
    count = 0
    for move in moves:
        print(f"move:{move} -> move-1:{move-1}")
        move += -1
        
        print(f"______________board______________")
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j],end=" ")
            print()
        print(f"______________board______________")

        for i in range(len(board)):
            if board[i][move] == 0:
                print(f"\tstack:{stack}")
                print(f"\tboard[{i}][{move}]:{board[i][move]} == 0")
            else:
                print(f"\tboard[{i}][{move}]:{board[i][move]} != 0")
                if(stack and stack[-1] == board[i][move]):
                    print(f"\t\tstack:{stack}")
                    print(f"\t\tstack[-1]:{stack[-1]} == board[{i}][{move}]:{board[i][move]} -> count:{count}+1={count+1} -> stack.pop -> break")
                    count+=1
                    stack.pop()
                    print(f"\t\tstack:{stack}")
                    break
                else:
                    print(f"\t\tstack:{stack}")
                    if stack:
                        print(f"\t\tstack[-1]:{stack[-1]} != board[{i}][{move}]:{board[i][move]} -> stack.append -> break")
                    stack.append(board[i][move])
                    print(f"\t\tstack:{stack}")
                    board[i][move] = 0
                    break
    print()
    return count * 2

print(f"______________before board______________")
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j],end=" ")
    print()
print(f"______________before board______________")

print(f"moves:{moves} result:{solution(board, moves)}")

print(f"______________after board______________")
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j],end=" ")
    print()
print(f"______________after board______________")