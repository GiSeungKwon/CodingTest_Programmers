str = input()
print(f"type(str): {type(str)} str: {str}")

list_str = list(str.replace("[","").replace("]","").split(','))
print(f"type(list_str): {type(list_str)} list_str: {list_str}")

def solution(param_list_str):
    print(f"type(param_list_str): {type(param_list_str)} list_str: {param_list_str}")
    if not(2 <= len(param_list_str) <= 10 ** 5):
        return "Exception"
    param_list_str.sort()
    # print(f"type(param_list_str): {type(param_list_str)} list_str: {param_list_str}")
    return param_list_str
print(f"solution(list_str): {solution(list_str)}")
print(f"list_str: {list_str}")