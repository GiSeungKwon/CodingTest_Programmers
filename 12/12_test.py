case1 = [1,2,3,2,3] # [4,3,1,1,0] 가격이 하락하지 않는 기간을 return

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