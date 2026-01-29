board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]
cmds = [1,5,3,5,1,2,1,4]

for i in range(len(board)):
    for j in range(len(board[0])):
        print(f"{board[i][j]} ", end="")
    print()

def solution(board, cmds):
    stack = []
    count = 0
    for cmd in cmds:
        cmd -= 1
        for i in range(len(board)):
            print(f"{cmd+1}->{cmd} board[{i}][{cmd}]: {board[i][cmd]}", end=" ")
            if board[i][cmd] != 0:
                if stack and stack[-1] == board[i][cmd]:
                    board[i][cmd] = 0
                    count += 1
                    stack.pop()
                    print(f"\tboard[i][cmd] != 0 and stack[-1]:{stack[-1]} == board[i][cmd]:{board[i][cmd]} -> stack.pop() stack: {stack} count+1:{count}")
                    break
                else:
                    stack.append(board[i][cmd])
                    print(f"\tboard[i][cmd] != 0 -> stack.append('{board[i][cmd]}') stack: {stack}")
                    board[i][cmd] = 0
                    break
            print()
    return count * 2

print(f"cmds:{cmds} result:{solution(board, cmds)}")