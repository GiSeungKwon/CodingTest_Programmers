case1 = [1,2,3,2,3] # [4,3,1,1,0] 가격이 하락하지 않는 기간을 return

def solution(prices):
    stack = []
    length = [0] * len(prices)

    for i, price in enumerate(prices):
        if not stack:
            stack.append(i)
        else:
            while stack and price < prices[stack[-1]]:
                poped_index = stack.pop()
                length[poped_index] = i-poped_index
            stack.append(i)

    for idx in stack:
        length[idx] = len(prices) - 1 - idx

    return length

print(case1, "->", solution(case1))