case1 = "ULURRDLLU" # 7
case2 = "LULLLLLLU" # 7

def solution(param_list):
    s = set()
    x, y =0, 0
    d = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    for item in param_list:
        nx, ny = x+d[item][0], y+d[item][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s)//2

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))