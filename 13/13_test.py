# 2차원 배열 board 5행(j) 5열(i)
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# 인형을 집는 크레인을 작동시킨 위치가 담긴 배열 moves
moves = [1,5,3,5,1,2,1,4]
# 크레인을 모두 작동시킨 후 사라진 인형 개수를 반환

def solution(board, moves):
    stack = []
    count = 0
    for move in moves:
        print(f"move:{move}", end=" -> ")
        move -= 1
        print(f"move -= 1:{move}")
        for i in range(len(board)):
            if board[i][move] != 0:
                if stack and stack[-1] == board[i][move]:
                    print(f"stack True stack[-1]:{stack[-1]} == board[{i}][{move}]:{board[i][move]} -> stack.pop()")
                    pop = stack.pop()
                    count += 1
                    board[i][move] = 0
                    print(f"stack.pop:{pop} -> stack:{stack} count:{count}")
                    break
                else:
                    stack.append(board[i][move])
                    print(f"board[{i}][{move}]:{board[i][move]} != 0 -> stack.append({board[i][move]}) -> stack:{stack}", end=" ")
                    board[i][move] = 0
                    print(f"board[{i}][{move}] = 0 -> board:{board}")
                    break
            else:
                print(f"board[{i}][{move}]:{board[i][move]} == 0")
        print()
    return count*2

print(f"board:{board} moves:{moves} result:{solution(board, moves)}")