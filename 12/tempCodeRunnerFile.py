case1 = [1,2,3,2,3]

def solution(prices):
    seconds = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        seconds[i] = count
    return seconds

print(case1, "->", solution(case1))