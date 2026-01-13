def solution(dirs):
    coordinate = [0, 0]
    move_coordinates = []
    length = 0
    for dir in dirs:
        if dir == "U":
            if coordinate[1] < 5:
                start = coordinate[:]
                coordinate[1] = coordinate[1] + 1
                end = coordinate[:]
                path = sorted([start, end])
                if path not in move_coordinates:
                    move_coordinates.append(path)
                    length += 1
        elif dir == "D":
            if coordinate[1] > -5:
                start = coordinate[:]
                coordinate[1] = coordinate[1] - 1
                end = coordinate[:]
                path = sorted([start, end])
                if path not in move_coordinates:
                    move_coordinates.append(path)
                    length += 1
        elif dir == "R":
            if coordinate[0] < 5:
                start = coordinate[:]
                coordinate[0] = coordinate[0] + 1
                end = coordinate[:]
                path = sorted([start, end])
                if path not in move_coordinates:
                    move_coordinates.append(path)
                    length += 1
        elif dir == "L":
            if coordinate[0] > -5:
                start = coordinate[:]
                coordinate[0] = coordinate[0] - 1
                end = coordinate[:]
                path = sorted([start, end])
                if path not in move_coordinates:
                    move_coordinates.append(path)
                    length += 1
    return length

# print(f"7 return 값: {solution('ULURRDLLU')}")
print(f"7 return 값: {solution('LULLLLLLU')}")