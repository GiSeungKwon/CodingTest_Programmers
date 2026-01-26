# 2차원 배열 board 5행(j) 5열(i)
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# 인형을 집는 크레인을 작동시킨 위치가 담긴 배열 moves
moves = [1,5,3,5,1,2,1,4]
# 크레인을 모두 작동시킨 후 사라진 인형 개수를 반환

def solution(board, moves):
    stack = []
    count = 0
    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                if stack and stack[-1] == board[i][move]:
                    pop = stack.pop()
                    count += 1
                    break
                else:
                    stack.append(board[i][move])
                    board[i][move] = 0
                    break
    return count*2

print(f"board:{board} moves:{moves} result:{solution(board, moves)}")