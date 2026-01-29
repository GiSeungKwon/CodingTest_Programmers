case1 = [1,2,3,2,3]

def solution(prices):
    stack = []
    period = [0] * len(prices)
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            period[j] = i - j
        stack.append(i)
    while stack:
        j = stack.pop()
        period[j] = len(prices) - 1 - j
    
    return period

print(case1, "->", solution(case1))
"""-------------------------------------------"""
# def solution(param_list):
#     return_list = []

#     for i, item in enumerate(param_list):
#         count = 0
#         for j in range(i+1, len(param_list)):
#             if item <= param_list[j]:
#                 count += 1
#             else:
#                 count += 1
#                 break 
#         return_list.append(count)
#     return return_list