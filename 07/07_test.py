case1 = "ULURRDLLU" # 7
case2 = "LULLLLLLU" # 7

def solution(move_commands):
    d = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0),}
    x, y = 0, 0
    path = set()
    for move_command in move_commands:
        nx, ny = x + d[move_command][0], y + d[move_command][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path.add((x,y,nx,ny))
            path.add((nx,ny,x,y))
            x, y = nx, ny
    return len(path)//2

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))