case1 = "ULURRDLLU" # 7
case2 = "LULLLLLLU" # 7

def solution(param_text):
    coordinate = [0, 0]
    path = []
    count = 0
    for i, item in enumerate(param_text):
        tmp_path = []
        if item == "U":
            if -5 < coordinate[1] < 5:
                tmp_path.append(coordinate[:])
                coordinate[1] += 1
                tmp_path.append(coordinate[:])
                if tmp_path not in path:
                    count += 1
                    path.append(tmp_path[:])
        elif item == "D":
            if -5 < coordinate[1] < 5:
                tmp_path.append(coordinate[:])
                coordinate[1] -= 1
                tmp_path.append(coordinate[:])
                if tmp_path not in path:
                    count += 1
                    path.append(tmp_path[:])
        elif item == "R":
            if -5 < coordinate[0] < 5:
                tmp_path.append(coordinate[:])
                coordinate[0] += 1
                tmp_path.append(coordinate[:])
                if tmp_path not in path:
                    count += 1
                    path.append(tmp_path[:])
        elif item == "L":
            if -5 < coordinate[0] < 5:
                tmp_path.append(coordinate[:])
                coordinate[0] -= 1
                tmp_path.append(coordinate[:])
                if tmp_path not in path:
                    count += 1
                    path.append(tmp_path[:])
        print(path)
    return count

print(case1, "->", solution(case1))
print(case2, "->", solution(case2))