case1 = [1,2,3,2,3]

def solution(param_list):
    return_list = []

    for i, item in enumerate(param_list):
        count = 0
        for j in range(i+1, len(param_list)):
            if item <= param_list[j]:
                count += 1
            else:
                count += 1
                break 
        return_list.append(count)
    return return_list

print(case1, "->", solution(case1))
"""-------------------------------------------"""
# case1 = [1,2,3,2,3]

# def solution(param_list):
#     result = []
#     for item in range(param_list):
#         if not result:
#             result.append(item)
#         else:
#             if result[-1] <= item:
#                 result.append(item)
#             else:
#                 break

# print(case1, "->", solution(case1))