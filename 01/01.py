str = input()
list_str = list(str.replace("[","").replace("]","").split(','))

def solution(param_list_str):
    return sorted(param_list_str)

def solution2(param_list_str):
    param_list_str.sort()
    return param_list_str

print(f"solution(list_str): {solution(list_str)}")
print(f"list_str: {list_str}")
print(f"solution2(list_str): {solution2(list_str)}")
print(f"list_str: {list_str}")