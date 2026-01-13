def solution(dirs):
    print(dirs)
    coordinate = [0, 0]
    move_coordinates = []
    length = 0
    for dir in dirs:
        if dir == "U":
            print(dir, end="->")
            if coordinate[1] >= 5:
                print(f"coordinate: {coordinate}", end=" ")
                print(f"Can't coordinate[1] + 1")
            else:
                print(f"coordinate: {coordinate}", end=" ")
                result_coordinate = []
                result_coordinate.append(coordinate[:])
                coordinate[1] = coordinate[1] + 1
                result_coordinate.append(coordinate[:])
                print(f"coordinate[1] + 1: {coordinate} result_coordinate: {result_coordinate}")
                if result_coordinate in move_coordinates:
                    print(f"이미 있는 좌표 coordinate: {coordinate}\t\tmove_coordinates: {move_coordinates}")
                else:
                    print(f"좌표 추가 result_coordinate: {result_coordinate}", end="\t\t")
                    move_coordinates.append(result_coordinate[:])
                    print(f"move_coordinates: {move_coordinates}")
                    length += 1
        elif dir == "D":
            print(dir, end="->")
            if coordinate[1] <= -5:
                print(f"coordinate: {coordinate}", end=" ")
                print(f"Can't coordinate[1] - 1")
            else:
                print(f"coordinate: {coordinate}", end=" ")
                result_coordinate = []
                result_coordinate.append(coordinate[:])
                coordinate[1] = coordinate[1] - 1
                result_coordinate.append(coordinate[:])
                print(f"coordinate[1] - 1: {coordinate} result_coordinate: {result_coordinate}")
                if result_coordinate in move_coordinates:
                    print(f"이미 있는 좌표 coordinate: {coordinate}\t\tmove_coordinates: {move_coordinates}")
                else:
                    print(f"좌표 추가 result_coordinate: {result_coordinate}", end="\t\t")
                    move_coordinates.append(result_coordinate[:])
                    print(f"move_coordinates: {move_coordinates}")
                    length += 1
        elif dir == "R":
            print(dir, end="->")
            if coordinate[0] >= 5:
                print(f"coordinate: {coordinate}", end=" ")
                print(f"Can't coordinate[0] + 1")
            else:
                print(f"coordinate: {coordinate}", end=" ")
                result_coordinate = []
                result_coordinate.append(coordinate[:])
                coordinate[0] = coordinate[0] + 1
                result_coordinate.append(coordinate[:])
                print(f"coordinate[0] + 1: {coordinate} result_coordinate: {result_coordinate}")
                if result_coordinate in move_coordinates:
                    print(f"이미 있는 좌표 coordinate: {coordinate}\t\tmove_coordinates: {move_coordinates}")
                else:
                    print(f"좌표 추가 result_coordinate: {result_coordinate}", end="\t\t")
                    move_coordinates.append(result_coordinate[:])
                    print(f"move_coordinates: {move_coordinates}")
                    length += 1
        elif dir == "L":
            print(dir, end="->")
            if coordinate[0] <= -5:
                print(f"coordinate: {coordinate}", end=" ")
                print(f"Can't coordinate[0] - 1")
            else:
                print(f"coordinate: {coordinate}", end=" ")
                result_coordinate = []
                result_coordinate.append(coordinate[:])
                coordinate[0] = coordinate[0] - 1
                result_coordinate.append(coordinate[:])
                print(f"coordinate[0] - 1: {coordinate} result_coordinate: {result_coordinate}")
                if result_coordinate in move_coordinates:
                    print(f"이미 있는 좌표 coordinate: {coordinate}\t\tmove_coordinates: {move_coordinates}")
                else:
                    print(f"좌표 추가 result_coordinate: {result_coordinate}", end="\t\t")
                    move_coordinates.append(result_coordinate[:])
                    print(f"move_coordinates: {move_coordinates}")
                    length += 1
    return length

# print(f"return 값: {solution('ULURRDLLU')}")
print(f"return 값: {solution('LULLLLLLU')}")