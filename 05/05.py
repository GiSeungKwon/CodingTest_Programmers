import ast
def to_list(param_str):
    arr1_str, arr2_str = param_str.split()
    return ast.literal_eval(arr1_str), ast.literal_eval(arr2_str)

def calc_matrix(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    result = [[0]*c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result

def solution():
    input_str = input()
    print(input_str)
    arr1, arr2 = to_list(input_str)
    return (lambda arr1, arr2: calc_matrix(arr1, arr2))(arr1, arr2)

print(solution())